<div class="page-thank-you">

<div class="row">
  <div class="col-md-3 hidden-xs hidden-sm scrollspy-target">

    <ul class="nav nav-list sbb-sidenav" data-spy="affix" data-offset-top="286" data-offset-bottom="270">
      <li class="active"><a href="#brands" class="nav-link"><i></i> <span>Brands</span></a></li>
      <li><a href="#personal" class="nav-link"><i></i> <span>Personal</span></a></li>
      <li>
        <?php include_once(drupal_get_path('theme', 'sbbtheme') . '/featured-sponsor/featured-sponsor.inc.php'); sbb_generate_featured_sponsor(); ?>
      </li>
    </ul>

  </div>
  <div class="col-md-9 content">

    <p class="description">We are lucky to have met some great people who are willing to support space research.</p>
    <p class="description">To all of these, we say:</p>

    <h3 class="thank-you">Thank you</h3>

    <section id="brands">
      <h2 class="page-header">Brands</h2>

      <ul class="brands">
<?php
include(drupal_get_path('theme', 'sbbtheme') . '/the-billboard/generated/customers_and_personal_messages.inc.php');
$added2Label = array();
foreach($sbb_customers as $label => $brand) {
  $added2Label[$brand['added']] = $label;
}
$dates = array_keys($added2Label);
sort($dates);
$nbSquares2Label = array();
foreach($dates as $date) {
  $label = $added2Label[$date];
  $brand = $sbb_customers[$label];
  if(! isset($nbSquares2Label[$brand['nbSquares']])) {
    $nbSquares2Label[$brand['nbSquares']] = array();
  }
  // put these in arrays that maintain order so the introduction date 
  // determines the order for brands with the same number of squares
  array_push($nbSquares2Label[$brand['nbSquares']], $label);
}
$numbers = array_keys($nbSquares2Label);
sort($numbers);
$numbers = array_reverse($numbers);
foreach($numbers as $number) {
  foreach($nbSquares2Label[$number] as $label) {
    $brand = $sbb_customers[$label];
    $plural = $brand['nbSquares'] == 1 ? '' : 's';
    echo('        <li><a href="' . $brand['url'] . '" target="_new">' . $brand['name'] . '</a> - ' . $brand['nbSquares'] . ' square' . $plural . '</li>');
  }
}
?>
      </ul>
    </section>

    <div class="visible-xs visible-sm">
      <?php sbb_generate_horizontal_featured_sponsor(); ?>
    </div>

    <section id="personal">
      <h2 class="page-header">Personal messages</h2>

<?php
include(drupal_get_path('theme', 'sbbtheme') . '/the-billboard/generated/customers_and_personal_messages.inc.php');
$reverted = array_reverse($sbb_personal_messages);
foreach($reverted as $msg) {
  $name = $msg['name'];
  if(! $msg['show_name_on_thankyou']) {
    $name = sbb_anonymize($name);
  }
  $to = $msg['to'];
  if(! $msg['show_name_on_thankyou']) {
    $to = sbb_anonymize($to);
  }
  $twitter = '';
  if($msg['show_twitter_on_thankyou'] && $msg['twitter_username']) {
    $twitter = '<a href="http://twitter.com/' . $msg['twitter_username'] . '" target="_new">@' . $msg['twitter_username'] . '</a>';
  }
  $url = '';
  if($msg['show_url_on_thankyou'] && $msg['url']) {
    $url = '<a href="' . $msg['url'] . '" target="_new">' . $msg['url'] . '</a>';
  }
  $data = '';
  if($twitter != '' || $url != '') {
    if($twitter != '' && $url != '') {
      $data = "$url, $twitter";
    } else {
      $data = "$url$twitter";
    }
  }
  if($msg['type'] == 'valentine') {
    $name = $name . ' <i class="fa fa-heart" style="color: #bf0000;"></i> ' . $to;
    $to = '';
  }
  echo("<h4>$name</h4><p>$to</p><p>$data</p><p>" . $msg['message'] . '</p>');
}
?>
    </section>

  </div>
</div>

</div> <!-- .page-thank-you -->
