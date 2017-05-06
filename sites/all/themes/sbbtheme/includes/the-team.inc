<div class="page-the-team">

<div class="row">
  <div class="col-md-3 hidden-xs hidden-sm scrollspy-target">

    <ul class="nav nav-list sbb-sidenav" data-spy="affix" data-offset-top="286" data-offset-bottom="270">
      <li>
        <?php include_once(drupal_get_path('theme', 'sbbtheme') . '/featured-sponsor/featured-sponsor.inc.php'); sbb_generate_featured_sponsor(); ?>
      </li>
    </ul>

  </div>
  <div class="col-md-9 content">

    <p class="description">SpaceBillboard is the initiative of<br/> <span class="accent">three PhD researchers in engineering</span><br/>of KU Leuven - Belgium:</p>

    <section id="brands">
      <img src="<?php sbb_echo_theme_file('resources/img/team/team.jpg'); ?>" class="img-responsive center-block team img-thumbnail" />

      <p class="names">From left to right: Maarten, Tjorven and Jeroen</p>
    </section>

    <div class="visible-xs visible-sm">
      <?php sbb_generate_horizontal_featured_sponsor(); ?>
    </div>

  </div>

</div> <!-- .page-the-team -->
