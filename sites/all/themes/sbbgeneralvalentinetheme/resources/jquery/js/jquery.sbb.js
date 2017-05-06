/**
 *	
 */
(function($) {
  if($.sbb == undefined) {
  	$.sbb = {};
  }
	$.sbb.facebook = {};

	var base = "/"; // we're using relative paths for now

	/**
	 *	Returns the full URL of the given resource.
	 *	Ex.: 'votes/facebook/add' -> http://spacebillboard.com/votes/facebook/add
	 *
	 *	@param	resource	The relative path of hte resource, NO LEADING '/'
	 */
	var full = function(resource) {
		return base + resource;
	};

  $.sbb.facebook.NetworkError = function(jqueryResult) {
      this.jqueryResult = jqueryResult;
      this.name = "NetworkError";
      this.message = "NetworkError";
  }
  $.sbb.facebook.NetworkError.prototype = new Error();
  $.sbb.facebook.NetworkError.prototype.constructor = $.sbb.facebook.NetworkError;
  NetworkError = $.sbb.facebook.NetworkError;

  $.sbb.facebook.AuthenticationError = function(message) {
      this.name = "AuthenticationError";
      this.message = message || "AuthenticationError";
  }
  $.sbb.facebook.AuthenticationError.prototype = new Error();
  $.sbb.facebook.AuthenticationError.prototype.constructor = $.sbb.facebook.AuthenticationError;
  AuthenticationError = $.sbb.facebook.AuthenticationError;

  $.sbb.facebook.AuthorizationError = function(message) {
      this.name = "AuthorizationError";
      this.message = message || "AuthorizationError";
  }
  $.sbb.facebook.AuthorizationError.prototype = new Error();
  $.sbb.facebook.AuthorizationError.prototype.constructor = $.sbb.facebook.AuthorizationError;
  AuthorizationError = $.sbb.facebook.AuthorizationError;

  $.sbb.facebook.CannotVoteYetError = function(timeBeforeNextVote) {
      this.name = "CannotVoteYetError";
      this.message = "CannotVoteYetError (time before next vote: " + timeBeforeNextVote + ")";
      this.timeBeforeNextVote = timeBeforeNextVote;
  }
  $.sbb.facebook.CannotVoteYetError.prototype = new Error();
  $.sbb.facebook.CannotVoteYetError.prototype.constructor = $.sbb.facebook.CannotVoteYetError;
  CannotVoteYetError = $.sbb.facebook.CannotVoteYetError;

  $.sbb.facebook.UnknownResultError = function(result) {
      this.name = "UnknownResultError";
      this.message = "UnknownResultError";
      this.result = result;
  }
  $.sbb.facebook.UnknownResultError.prototype = new Error();
  $.sbb.facebook.UnknownResultError.prototype.constructor = $.sbb.facebook.UnknownResultError;
  UnknownResultError = $.sbb.facebook.UnknownResultError;

	/**
	 *	Calls the URL, evaluates the JSON returned and returns the result value as JS object on success.
	 *
	 *	@param	destination			Location of the destination (String URL)
	 *	@param	success: function(result: Object)	Callback on success. Will be called 
   *            with the result value (excluding the result type) as JS object.
	 *	@param	error: function(e: Exception)	Callback on error (in case of network 
   *            error or result.value == "error"). The error will an instance of NetworkError.
	 */
	var jsonCall = function(destination, success, error) {
		$.ajax({
			url: destination,
			dataType: "json",
			type: "GET",
			success: function(result) {
				success(result);
			},
      error: function(result) {
        error(new NetworkError(result)); // FIXME is the network error really the only possible reason for error?
      }
		});
	};

  /**
   *  Calls the given relative URL in the domain and returns the result.
   *  
	 *	@param	destination			Location of the destination (String URL)
	 *	@param	success: function(result: Object)	Callback on success. Will be called 
   *            with the result value (excluding the result type) as JS object.
	 *	@param	error: function(e: Exception)	Callback on error (in case of network 
   *            error or result.value == "error"). The error will an instance of be one 
   *            of the following:
   *              - NetworkError
   *              - AuthenticationError
   *              - AuthorizationError
   *              - CannotVoteYetException
   *              - UnknownResultException
	 */
  var callServer = function(destination, success, error) {	
		var url = full(destination);
    jsonCall(url, function(result) {
      if(result.type == "success") {
        success(result.value);
      } else if(result.type == "error") {
        if(result.value.name == "AuthenticationException") {
          error(new AuthenticationError());
        } else if(result.value.name == "AuthorizationException") {
          error(new AuthorizationError());
        } else if(result.value.name == "CannotVoteYetException") {
          error(new CannotVoteYetError(result.value.timeBeforeNextVote));
        } else {
          error(new UnknownResultError(result));
        }
      } else {
        error(new UnknownResultError(result));
      }
    }, function(e) {
      error(e); // e will be the NetworkError
    });
  }

	/**
	 *	Returns whether the user can vote now and if not, the time left before he can vote again
   *  in seconds.
	 *	
	 *	@param	success: function(canVote: boolean, timeToNext: int) 
   *            Note: timeToNext only included if canVote == false;
	 *	@param	error: function(e: Exception)	Callback on error (in case of network 
   *            error or result.value == "error"). The error will an instance of be one 
   *            of the following:
   *              - NetworkError
   *              - AuthenticationError
   *              - UnknownResultException
	 *
	$.sbb.facebook.canVoteNow = function(success, error) {	
		callServer("votes/facebook/can-vote-now", function(result) {
      if(result.canVote == true) {
        success(true);
      } else {
        success(true, result.timeBeforeNextVote);
      }
    }, function(e) {
      error(e);
    }); 
	};

	/**
	 *	Votes for the user and returns whether the vote was succesful.
	 *	
	 *	@param	success: function()
	 *	@param	error: function(e: Exception)	Callback on error (in case of network 
   *            error or result.value == "error"). The error will an instance of be one 
   *            of the following:
   *              - NetworkError
   *              - AuthenticationError
   *              - AuthorizationError
   *              - CannotVoteYetException
   *              - UnknownResultException
	 */
	$.sbb.facebook.vote = function(success, error) {
		callServer("sbbvoting/facebook/add", function(result) {
      success();
    }, function(e) {
      error(e);
    }); 
	};
})(jQuery);
