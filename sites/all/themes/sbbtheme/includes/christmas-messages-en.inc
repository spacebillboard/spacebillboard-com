<?php
$theme_path = drupal_get_path('theme', 'sbbtheme');
drupal_add_js($theme_path . '/resources/jquery/js/bootstrapValidator.js');
drupal_add_css($theme_path . '/resources/css/bootstrapValidator.min.css', array('weight' => -10));
?>

<div class="christmas-messages">

<div class="text-right"><small>English - <a href="/kerstwensen">Nederlands</a></small></div>

<h3 class="text-center" id="order">What do you get?</h3>

<div class="row">
  <div class="col-md-4">
    <img src="<?php sbb_echo_theme_file('resources/img/xmas-messages/cubesat.jpg'); ?>" id="" class="img-responsive img-thumbnail md-pull-right center-block-below-md" style="max-height:200px;margin-top:32px;"/>    
  </div>
  <div class="col-md-8 text-left">
    <h4 class="center-below-md">Your Christmas wishes in space</h4>
    <p>We launch your Christmas wishes into space as part of our billboard. That way, your wishes will <span class="accent">orbit the Earth 15 times a day for years to come</span>! And of course, we also show them <span class="accent">on this website as well.</span></p>
  </div>
</div>
<div class="row">
  <div class="col-md-4 icon-container">
    <img src="<?php sbb_echo_theme_file('resources/img/xmas-messages/physical-en.jpg'); ?>" id="" class="img-responsive img-thumbnail md-pull-right center-block-below-md" style="max-height:200px;margin-top:32px;"/>
  </div>
  <div class="col-md-8 text-left">
    <h4 class="center-below-md">A Christmas card for you to print</h4>
    <p>Of course you also receive an actual <span class="accent">Christmas card</span>. Or more precisely, we provide you with the design of your personalized Christmas card from space that you can print yourself and <span class="accent">send to as many people as you want</span>.</p>
    <p>&gt; <a href="<?php sbb_echo_theme_file('resources/img/xmas-messages/example-en.png'); ?>" target="_new" class="">Example</a></p>
  </div>
</div>
<div class="row">
  <div class="col-md-4">
    <img src="<?php sbb_echo_theme_file('resources/img/xmas-messages/ecard-en.jpg'); ?>" id="" class="img-responsive img-thumbnail md-pull-right center-block-below-md" style="max-height:250px;margin-top:32px;"/>
  </div>
  <div class="col-md-8 text-left">
    <h4 class="center-below-md">A Christmas e-card for you to e-mail</h4>
    <p>Would you rather send out your Christmas card electronically? We also provide you with your <span class="accent">personalized Christmas e-card</span>!</p>
    <p>&gt; <a href="<?php sbb_echo_theme_file('resources/img/xmas-messages/ecard-large-en.jpg'); ?>" target="_new" class="">Example</a></p>
  </div>
</div>

<h3 class="text-center" id="order">What does it cost?</h3>
<p style="text-align:center;font-size:20px;">Only <span class="accent">&euro;1/character</span> of your Christmas wishes!</p>

<h2 class="page-header" id="order">Ready? Get your Christmas card!</h2>

<form class="form-horizontal" role="form"  id="buyForm" action="/christmas-messages/initiate-purchase" method="post">
  <div class="form-group">
    <label for="to" class="col-sm-3 control-label">To</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="to" name="to" placeholder="The recipient of your Christmas card, plus salutation" maxlength="30" />
      <p><small>You receive a single design of your personalized Christmas card, but of course you can address it to multiple people and send it multiple times! For example, &quot;Hi Tim&quot;, or &quot;Dear Alice and David&quot;, or &quot;To my family&quot;.</small></p>
    </div>
  </div>
  <div class="form-group">
    <label for="message" class="col-sm-3 control-label">Your wish</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="message" name="message" placeholder="I wish you..." maxlength="140" />
      <div id="total" class="accent"><span class="characters">0</span> character<span class="plural">s</span> = &euro; <span class="cost">0</span> <small>(incl. VAT)</small></div>
    </div>
  </div>
  <div class="form-group">
    <label for="from" class="col-sm-3 control-label">From</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="from" name="from" placeholder="Your name" maxlength="30" />
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="plural" name="plural"> This name is plural <small>(we have to know this to get the text on your card right)</small>
      </label>
    </div>
  </div>
  <div class="form-group">
    <label for="email" class="col-sm-3 control-label">Your email address</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="email" name="email" placeholder="This is where we will send your Christmas card to" />
      <input type="text" class="form-control" id="email2" name="email2" placeholder="Please repeat your email address" style="margin-top:15px;"/>
    </div>
  </div>
  <div class="form-group">
    <label for="twitter" class="col-sm-3 control-label">Optionally: your Twitter username</label>
    <div class="col-sm-6">
      <div class="input-group">
        <div class="input-group-addon">@</div>
        <input type="text" class="form-control" id="twitter" name="twitter" placeholder="We'll tweet our thanks as well (if you want)" />
      </div>
    </div>
  </div>
  <div class="form-group">
    <label for="url" class="col-sm-3 control-label">Optionally: your homepage</label>
    <div class="col-sm-6">
      <div class="input-group">
        <div class="input-group-addon">http://</div>
        <input type="text" class="form-control" id="url" name="url" placeholder="example.com" />
      </div>
    </div>
  </div>
  <div class="form-group">
    <label for="" class="col-sm-3 control-label">How can we show our gratitude on the Thank You page?</label>
    <div class="col-sm-6">
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="show-name" name="show-name" checked> Show my name
      </label>
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="show-twitter" name="show-twitter" disabled="disabled"> Show my Twitter username
      </label>
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="show-url" name="show-url" disabled="disabled"> Show my homepage
      </label>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-3 col-sm-6">
      <button type="submit" id="submitFrontendForm" class="btn btn-primary">Pay now with PayPal, VISA or MasterCard</button>
    </div>
  </div>
</form>

<!--<form id="buyForm" action="/christmas-messages/initiate-purchase" method="post">
  <div class="field">
    <div class="row text-center message">
      <div class="col-xs-12 col-md-6 col-md-offset-3">
        <label for="to"><h4>To</h4></label>
        <div class="form-group">
            <input type="text" class="form-control" id="to" name="to" placeholder="The recipient(s) of your Christmas card" maxlength="30" />
        </div>
      </div>
    </div>
  </div>
  <div class="field">
    <div class="row text-center message">
      <div class="col-xs-12 col-md-6 col-md-offset-3">
        <label for="message"><h4>Your message</h4></label>
        <div class="form-group">
            <input type="text" class="form-control" id="message" name="message" placeholder="Your message" maxlength="140" />
        </div>
      </div>
    </div>
    <div class="row text-center">
      <div class="col-md-12 col-sm-12 col-xs-12">
        <div id="total" class="accent"><span class="characters">0</span> character<span class="plural">s</span> = &euro; <span class="cost">0</span><br/>(incl. VAT)</div>
      </div>
    </div>
  </div>
  <div class="row field text-center message">
    <div class="col-xs-12 col-md-6 col-md-offset-3">
      <label for="from"><h4>From</h4></label>
      <div class="form-group">
          <input type="text" class="form-control" id="from" name="from" placeholder="Your name" maxlength="30" />
      </div>
      <div class="checkbox text-left">
        <label>
          <input type="checkbox" id="plural" name="plural"> This is plural <small>(needed so we can get the text on your card right)</small>
        </label>
      </div>
    </div>
  </div>
  <div class="row field text-center message">
    <div class="col-xs-12 col-md-6 col-md-offset-3">
      <label for="email"><h4>Your email address</h4></label>
      <div class="form-group">
          <input type="text" class="form-control" id="email" name="email" placeholder="Your email address" />
      </div>
      <label class="sr-only" for="email2">Repeat email address</label>
      <div class="form-group">
          <input type="text" class="form-control" id="email2" name="email2" placeholder="Repeat your email address" />
      </div>
      <div class="subtext">This is where your Christmas card and certificate will be sent to.</div>
    </div>
  </div>
  <div class="row field text-center message form-inline">
    <div class="col-xs-12 col-md-6 col-md-offset-3">
      <label for="twitter"><h4>Optionally: your Twitter username</h4></label>
      <div class="form-group" style="margin-bottom: 15px;">
        <div class="input-group">
          <div class="input-group-addon">@</div>
          <input type="text" class="form-control" id="twitter" name="twitter" placeholder="Your Twitter username" />
        </div>
      </div>
      <div class="subtext">We'll tweet our thanks as well.</div>
    </div>
  </div>
  <div class="row field text-center message form-inline">
    <div class="col-xs-12 col-md-6 col-md-offset-3">
      <label for="twitter"><h4>Optionally: your homepage</h4></label>
      <div class="form-group" style="margin-bottom: 15px;">
        <div class="input-group">
          <div class="input-group-addon">http://</div>
          <input type="text" class="form-control" id="url" name="url" placeholder="Your homepage URL" />
        </div>
      </div>
      <div class="subtext">To show on the Thank You page (if you want).</div>
    </div>
  </div>
  <div class="row field text-center message form-inline">
    <div class="col-xs-12 col-md-6 col-md-offset-3">
      <h4>Show me on the Thank You page</h4>
      <div class="row">
        <div class="col-sm-6 text-left">
          <div class="checkbox">
            <label>
              <input type="checkbox" id="show-name" name="show-name" checked> Show my name
            </label>
          </div>
        </div>
        <div class="col-sm-6 text-left">
          <div class="checkbox">
            <label>
              <input type="checkbox" id="show-url" name="show-url" disabled="disabled"> Show my homepage
            </label>
          </div>
        </div>
        <div class="col-sm-6 text-left">
          <div class="checkbox">
            <label>
              <input type="checkbox" id="show-twitter" name="show-twitter" disabled="disabled"> Show my Twitter username
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row field text-center">
    <div class="col-md-6 col-md-offset-3 col-sm-12 col-xs-12">
      <div class="form-group">
        <button type="submit" id="submitFrontendForm" class="btn btn-primary" disabled="disabled">Pay now with PayPal, VISA or MasterCard</button>
      </div>
    </div>
  </div>
</form>-->


</div> <!-- .personal-messages -->

<script>
(function($){
  // form validation
  $('#buyForm').bootstrapValidator({
      message: 'This value is not valid',
      submitButtons: "#submitFrontendForm",
      live: 'submitted',
      fields: {
            message: {
                message: 'Your wish is not valid',
                validators: {
                    notEmpty: {
                        message: 'A Christmas wish is required and cannot be empty'
                    }
                }
            },
            from: {
                message: 'Your name is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your name is required and cannot be empty'
                    }
                }
            },
            to: {
                message: 'Your recipient is not valid',
                validators: {
                    notEmpty: {
                        message: 'A recipient is required and cannot be empty'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Your email is required and cannot be empty'
                    },
                    emailAddress: {
                        message: 'The input is not a valid email address'
                    }
                }
            },
            email2: {
                validators: {
                    notEmpty: {
                        message: 'Please repeat your email address'
                    },
                    emailAddress: {
                        message: 'The input is not a valid email address'
                    },
                    identical: {
                        field: 'email',
                        message: 'The email addresses are not the same'
                    }
                }
            }
      }
  });
  // enable or disable the "show Twitter username" depending on whether it is filled in or not
  var updateShowTwitter = function() {
    if($("#twitter").val().length > 0) {
      console.log("twitter is not empty: " + $("#show-twitter").val());
      $("#show-twitter").removeAttr("disabled");
    } else {
      $("#show-twitter").attr("disabled","disabled");
    }
  };
  $("#twitter").keyup(updateShowTwitter);
  $("#twitter").change(updateShowTwitter);
  // enable or disable the "show homepage" depending on whether it is filled in or not
  var updateShowURL = function() {
    if($("#url").val().length > 0) {
      $("#show-url").removeAttr("disabled");
    } else {
      $("#show-url").attr("disabled","disabled");
    }
  };
  $("#url").keyup(updateShowURL);
  $("#url").change(updateShowURL);
  // validate the form at page load (for when the user clicked Back)
  var buyFormNotEmpty = function() {
    var notEmpty = false;
    $("#buyForm input:text").each(function() {
      if($(this).val()) {
        notEmpty = true;
      }
    });
    return notEmpty;
  };
  if(buyFormNotEmpty()) {
    console.log('validated');
    $("#buyForm").bootstrapValidator('validate');
    updateShowTwitter();
    updateShowURL();
  }

  // for the cost updates
  var formAPI = {
    updatePrice: function() {
      var nbCharacters = $("#message").val().length;
      var cost = nbCharacters * 1;
      var plural = function(value) {
        if(value == 0 || value > 1) {
          return "s";
        } else {
          return "";
        }
      };
      // visible values
      $("#total .characters").html(nbCharacters);
      $("#total .plural").html(plural(nbCharacters));
      $("#total .cost").html(cost); // €1/character
      // paypal
      $("#quantity").val(cost);
    }
  };
  $("#message").keyup(function() {
    formAPI.updatePrice();
  });
  $("#message").change(function() {
    formAPI.updatePrice();
  });

  // update the price immediately (for when the user pressed return in PayPal)
  formAPI.updatePrice();
})(jQuery);
</script>
