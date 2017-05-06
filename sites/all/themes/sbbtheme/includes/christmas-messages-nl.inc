<?php
$theme_path = drupal_get_path('theme', 'sbbtheme');
drupal_add_js($theme_path . '/resources/jquery/js/bootstrapValidator.js');
drupal_add_css($theme_path . '/resources/css/bootstrapValidator.min.css', array('weight' => -10));
?>

<div class="christmas-messages">

<div class="text-right"><small><a href="/christmas-wishes">English</a> - Nederlands</small></div>

<h3 class="text-center" id="order">Wat krijg je?</h3>

<div class="row">
  <div class="col-md-4">
    <img src="<?php sbb_echo_theme_file('resources/img/xmas-messages/cubesat.jpg'); ?>" id="" class="img-responsive img-thumbnail md-pull-right center-block-below-md" style="max-height:200px;margin-top:32px;"/>    
  </div>
  <div class="col-md-8 text-left">
    <h4 class="center-below-md">Jouw Kerstwensen in de ruimte</h4>
    <p>We lanceren jouw Kerstwensen in de ruimte als deel van ons <i>billboard</i>. Op die manier blijven je wensen <span class="accent">in een baan rond de Aarde voor jaren</span> en <span class="accent">gaan ze elke dag 15 keer de wereld rond</span>! En natuurlijk tonen we ze ook <span class="accent">op deze website.</span></p>
  </div>
</div>
<div class="row">
  <div class="col-md-4 icon-container">
    <img src="<?php sbb_echo_theme_file('resources/img/xmas-messages/physical-en.jpg'); ?>" id="" class="img-responsive img-thumbnail md-pull-right center-block-below-md" style="max-height:200px;margin-top:32px;"/>
  </div>
  <div class="col-md-8 text-left">
    <h4 class="center-below-md">Een Kerstkaart om zelf te printen</h4>
    <p>Uiteraard ontvang je ook een echte <span class="accent">Kerstkaart</span>. Of meer precies, krijg je van ons het ontwerp van je gepersonaliseerde Kerstkaart die je zelf kan printen en naar <span class="accent">zoveel mensen kan zenden als je zelf wilt</span>.</p>
    <p>&gt; <a href="<?php sbb_echo_theme_file('resources/img/xmas-messages/example-nl.png'); ?>" target="_new" class="">Voorbeeld</a></p>
  </div>
</div>
<div class="row">
  <div class="col-md-4">
    <img src="<?php sbb_echo_theme_file('resources/img/xmas-messages/ecard-nl.jpg'); ?>" id="" class="img-responsive img-thumbnail md-pull-right center-block-below-md" style="max-height:250px;margin-top:32px;"/>
  </div>
  <div class="col-md-8 text-left">
    <h4 class="center-below-md">Een Kerstkaart om te e-mailen</h4>
    <p>Zend je je Kerstkaarten liever elektronisch? Je krijgt ook je eigen <span class="accent">gepersonaliseerde e-card</span>!</p>
    <p>&gt; <a href="<?php sbb_echo_theme_file('resources/img/xmas-messages/ecard-large-nl.jpg'); ?>" target="_new" class="">Voorbeeld</a></p>
  </div>
</div>

<h3 class="text-center" id="order">Hoeveel kost het?</h3>
<p style="text-align:center;font-size:20px;">Slechts <span class="accent">&euro;1/karakter</span> van je Kerstwensen!</p>

<h2 class="page-header" id="order">Klaar? Bestel nu je Kerstkaart!</h2>

<form class="form-horizontal" role="form"  id="buyForm" action="/christmas-messages/initiate-purchase" method="post">
  <div class="form-group">
    <label for="to" class="col-sm-3 control-label">Aan</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="to" name="to" placeholder="De ontvanger van je Kerstkaart, m&eacute;t aanhef" maxlength="30" />
      <p><small>Je ontvangt &eacute;&eacute;n enkel ontwerp van je Kerstkaart, maar je kan dit uiteraard aan meerdere mensen richten en meerdere keren versturen! Bijvoorbeeld &quot;Aan David&quot;, of &quot;Hey Ilse en Kobe&quot;, of &quot;Beste familie&quot;.</small></p>
    </div>
  </div>
  <div class="form-group">
    <label for="message" class="col-sm-3 control-label">Your wish</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="message" name="message" placeholder="I wish you..." maxlength="140" />
      <div id="total" class="accent"><span class="characters">0</span> karakter<span class="plural">s</span> = &euro; <span class="cost">0</span> <small>(incl. BTW)</small></div>
    </div>
  </div>
  <div class="form-group">
    <label for="from" class="col-sm-3 control-label">Van</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="from" name="from" placeholder="Jouw of jullie naam" maxlength="30" />
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="plural" name="plural"> Deze naam is meervoud <small>(we hebben dit nodig om de tekst op je kaart juist te krijgen)</small>
      </label>
    </div>
  </div>
  <div class="form-group">
    <label for="email" class="col-sm-3 control-label">Je e-mailadres</label>
    <div class="col-sm-6">
      <input type="text" class="form-control" id="email" name="email" placeholder="Hiernaar zenden we je Kerstkaart" />
      <input type="text" class="form-control" id="email2" name="email2" placeholder="Herhaal je e-mailadres aub." style="margin-top:15px;"/>
    </div>
  </div>
  <div class="form-group">
    <label for="twitter" class="col-sm-3 control-label">Optioneel: je Twitter username</label>
    <div class="col-sm-6">
      <div class="input-group">
        <div class="input-group-addon">@</div>
        <input type="text" class="form-control" id="twitter" name="twitter" placeholder="We zullen onze dank ook Tweeten (als je wilt)" />
      </div>
    </div>
  </div>
  <div class="form-group">
    <label for="url" class="col-sm-3 control-label">Optioneel: je homepage</label>
    <div class="col-sm-6">
      <div class="input-group">
        <div class="input-group-addon">http://</div>
        <input type="text" class="form-control" id="url" name="url" placeholder="example.be" />
      </div>
    </div>
  </div>
  <div class="form-group">
    <label for="" class="col-sm-3 control-label">Hoe mogen we onze dankbaarheid tonen op de Thank You pagina?</label>
    <div class="col-sm-6">
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="show-name" name="show-name" checked> Toon mijn naam
      </label>
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="show-twitter" name="show-twitter" disabled="disabled"> Toon mijn Twitter username
      </label>
      <label style="width:100%;text-align:left;font-weight:normal;padding-left:0px;">
        <input type="checkbox" id="show-url" name="show-url" disabled="disabled"> Toon mijn homepage
      </label>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-3 col-sm-6">
      <button type="submit" id="submitFrontendForm" class="btn btn-primary">Betaal nu met PayPal, VISA of MasterCard</button>
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
