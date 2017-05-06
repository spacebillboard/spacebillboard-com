<?php
drupal_add_css($theme_path . '/resources/css/bootstrap-social.css');
?>

<div class="page-contest">

<h1 class="real-page-title page-header">Win a two-week trip to the launch!</h1>

<div class="row">
  <div class="col-md-3 hidden-xs hidden-sm scrollspy-target">

    <ul class="nav nav-list sbb-sidenav" data-spy="affix" data-offset-top="286" data-offset-bottom="270">
      <li class="active"><a href="#image-carousel" class="nav-link"><i></i> <span>Top</span></a></li>
      <li><a href="#participating" class="nav-link"><i></i> <span>Participating</span></a></li>
      <li><a href="#the-prize" class="nav-link"><i></i> <span>The prize</span></a></li>
      <li>
        <?php include_once(drupal_get_path('theme', 'sbbtheme') . '/featured-sponsor/featured-sponsor.inc.php'); sbb_generate_featured_sponsor(); ?>
      </li>
    </ul>

  </div>
  <div class="col-md-9 content">

      <div id="image-carousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#image-carousel" data-slide-to="0" class="active"></li>
          <li data-target="#image-carousel" data-slide-to="1"></li>
          <li data-target="#image-carousel" data-slide-to="2"></li>
        </ol>
        <!-- Carousel items -->
        <div class="carousel-inner">
          <div class="active item">
           <img src="<?php sbb_echo_theme_file('resources/img/contest/rocketlaunch.jpg'); ?>"/>
           <div class="carousel-caption">
             <h4>Join us to the rocket launch!</h4>
           </div>
          </div>
          <div class="item">
           <img src="<?php sbb_echo_theme_file('resources/img/contest/two-people.jpg'); ?>"/>
           <div class="carousel-caption">
             <h4>Bring a friend. Lay back and enjoy your two-week holiday.</h4>
           </div>
          </div>
          <div class="item">
           <img src="<?php sbb_echo_theme_file('resources/img/contest/plane.jpg'); ?>"/>
           <div class="carousel-caption">
             <h4>We pay everything. All you need to do, is get on the plane.</h4>
           </div>
          </div>
        </div>
      </div>

      <p class="description"><span class="accent">Shared happiness is double happiness.</span> That is why we want you to join us to see a rocket take off in <span class="accent">Alc&acirc;ntara, Brazil</span>. And since watching a launch is an exhilarating experience, we also give you a <span class="accent">two-week stay</span> to relax after the launch. <span class="accent">For free and flight included.</span> From whereever you live on Earth.</p>

      <h2 class="page-header" id="participating">Participating</h2>

      <p class="description">We will announce the contest somewhere in the future, but to give you a hint:<br/><span class="accent">the contest will involve our followers</span> :)</p>

      <p class="description">So be sure to follow us already!</p>

      <div class="row follow-buttons">
        <div class="col-xs-4 col-xs-offset-2">
          <a href="https://www.facebook.com/spacebillboarddotcom" target=_new" id="follow-on-facebook-btn" class="btn btn-social btn-facebook btn-block">
            <i class="fa fa-facebook"></i> Follow us <span class="hidden-md-inline">on Facebook</span>
          </a>
        </div> 
        <div class="col-xs-4">
          <a href="https://twitter.com/intent/user?user_id=2210568709" target=_new" class="btn btn-social btn-twitter btn-block">
            <i class="fa fa-twitter"></i> Follow us <span class="hidden-md-inline">on Twitter</span>
          </a>
        </div> 
      </div>

      <div class="visible-xs visible-sm">
        <?php sbb_generate_horizontal_featured_sponsor(); ?>
      </div>

      <h2 class="page-header" id="the-prize">The prize!</h2>

      <div class="row prize-items">
        <div class="row">
          <div class="col-md-4 col-sm-4 col-xs-4 image text-center"><img src="<?php sbb_echo_theme_file('resources/img/contest/airplane.png'); ?>" width="180" height="180" alt=""  data-thmr="thmr_68" /></div>
          <div class="col-md-8 col-sm-8 col-xs-8">
            <h3>Your flight</h3>
            <p>We pay your flight from where ever you are to Brazil - and back.</p>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-sm-4 col-xs-4 image text-center"><img src="<?php sbb_echo_theme_file('resources/img/contest/rocket.png'); ?>" width="180" height="180" alt="" class="" data-thmr="thmr_14" /></div>
          <div class="col-md-8 col-sm-8 col-xs-8">
            <h3>Rocket launch</h3>
            <p>Watching a rocket launch is an incredible experience that will stick with you for the rest of your life!  </p>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-sm-4 col-xs-4 image text-center"><img src="<?php sbb_echo_theme_file('resources/img/contest/beach.png'); ?>" width="180" height="180" alt="" class="" data-thmr="thmr_20" /></div>
          <div class="col-md-8 col-sm-8 col-xs-8">
            <h3>Your stay</h3>
            <p>Your two-week stay in a nice hotel is covered as well. Just relax and have a cocktail on the beach, we even pay that!</p>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-sm-4 col-xs-4 image text-center"><img src="<?php sbb_echo_theme_file('resources/img/contest/two-persons.png'); ?>" width="180" height="180" alt="" class="" data-thmr="thmr_20" /></div>
          <div class="col-md-8 col-sm-8 col-xs-8">
            <h3>Two persons</h3>
            <p>Bring a friend. It would be a shame to have to enjoy all of this on your own, no?</p>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-sm-4 col-xs-4 image text-center"><img src="<?php sbb_echo_theme_file('resources/img/contest/relax.png'); ?>" width="180" height="180" alt="" class="" data-thmr="thmr_20" /></div>
          <div class="col-md-8 col-sm-8 col-xs-8">
            <h3>No strings attached</h3>
            <p>When we say "no strings attached," we really mean it. Just bring your good mood and enough clothes. <!--But because we officially need some fine prints, you can find them <a href="/contest-terms-and-conditions">here</a>.--></p>
          </div>
        </div>
      </div>

  </div>
</div>

</div> <!-- .page-contest -->
