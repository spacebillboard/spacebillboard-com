<?php
$theme_path = drupal_get_path('theme', 'sbbtheme');
drupal_add_js($theme_path . '/resources/jquery/js/bootstrapValidator.js');
drupal_add_css($theme_path . '/resources/css/bootstrapValidator.min.css', array('weight' => -10));
?>

<div class="personal-messages">



  <div class="row text-center">
    <div class="col-xs-12 col-md-offset-2 col-md-8 col-lg-offset-3 col-lg-6" id="">
      <section id="" style="margin-bottom:100px;">
        <p class="description">Next to brands putting their logo on the billboard, we also want to allow everyone to <span class="accent">send their personal message to space</span> and get it around the world!</p>
      </section>
    </div>
  </div>

<div class="row sm-center">
  <div class="col-md-3 icon-container">
    <img src="<?php sbb_echo_theme_file('resources/img/buy-squares/arrow-right.png'); ?>" id="question-arrow" class="hidden-xs hidden-sm center-block"/>
    <img src="<?php sbb_echo_theme_file('resources/img/buy-squares/question.png'); ?>" class="hidden-md hidden-lg center-block"/>
  </div>
  <div class="col-md-9">
    <h3>How does it work?</h3>
    <p>You choose a message of <span class="accent">max 140 characters</span> and we get it into space, it's as simple as that. And because we want to honor the fact that you supported space research, we also send you a <span class="accent">personal certificate</span> afterwards.</p>
    <p><a href="<?php sbb_echo_theme_file('resources/img/front/certificate-large.jpg'); ?>" target="_new"><img src="<?php sbb_echo_theme_file('resources/img/front/certificate-small.jpg'); ?>" class="img-responsive img-thumbnail" id="certificate"></img></a></p>
  </div>
</div> 
<div class="row sm-center">
  <div class="col-md-3 icon-container">
    <img src="<?php sbb_echo_theme_file('resources/img/personal-messages/gift.png'); ?>" id="media"/>
  </div>
  <div class="col-md-9">
    <h3>Can I donate the certificate to someone else?</h3>
    <p>Of course! The certificate is <span class="accent">the perfect gift to any space enthousiast</span>.</p>
  </div>
</div> 
<div class="row sm-center">
  <div class="col-md-3 icon-container">
    <img src="<?php sbb_echo_theme_file('resources/img/personal-messages/coin.png'); ?>" id="media"/>
  </div>
  <div class="col-md-9">
    <h3>How much does this cost?</h3>
    <p>For a personal message, we charge <span class="accent">&euro;1 per character</span>. For example, the message &ldquo;happy birthday Hannah!&rdquo; counts 22 characters and would cost &euro;22.</p>
  </div>
</div>

<h2 class="page-header" id="order">Ready? Put your message on the billboard!</h2>

<p class="description">Too bad, submissions were closed on July 1st 2015.</p>
<p class="description">We're getting the billboard ready for the launch now!</p>


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
                message: 'Your message is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your message is required and cannot be empty'
                    }
                }
            },
            name: {
                message: 'Your name is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your name is required and cannot be empty'
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
                        message: 'Your email is required and cannot be empty'
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
