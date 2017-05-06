<?php
/**
 *  SUPPORT
 */
module_load_include('inc','webform','includes/webform.submissions');
module_load_include('inc.php','sbbpersonalmsg','classes/PurchaseWebformSubmission');

/**
 *  Get the submissions, grouped by id.
 */
$raw_submissions = webform_get_submissions(array('nid'=>variable_get('sbbgoodcauses_votes_webform_id')));
$submissions = array();
foreach($raw_submissions as $submission) {
  $id = $submission->data[1]['value'][0];
  if(isset($submissions[$id])) {
    $reason = $submission->data[4]['value'][0];
    array_push($submissions[$id]['reasons'],$reason);
  } else {
    $submissions[$id] = array(
      "id" => $submission->data[1]['value'][0],
      "name" => $submission->data[2]['value'][0],
      "url" => $submission->data[3]['value'][0],
      "reasons" => array($submission->data[4]['value'][0])
    );
  }
}
?>

<div class="row text-center">
  <div class="col-xs-12 col-md-offset-2 col-md-8" id="">
  <p class="accent"><?php echo(count($raw_submissions)); ?> nominations received for now</p>
  <div class="row text-center">
    <div class="col-xs-8 col-xs-offset-2 col-md-offset-4 col-md-4" id="">
      <form>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search a good cause" id="search-good-cause">
        </div>
      </form>
    </div>
  </div>
<?php 
$keys = array_keys($submissions);
sort($keys);
foreach($keys as $id) { 
  $s = $submissions[$id];
?>
  <div>
    <h3 style="margin-top:70px;" class="accent-blue good-cause-name"><?php echo($s['name']); ?></h3>
    <p><a href="/" class="good-cause-link" data-good-cause-id="<?php echo($id); ?>" data-good-cause-name="<?php echo($s['name']); ?>" data-good-cause-url="<?php echo($s['url']); ?>">Support them too</a></p>
    <?php foreach($s['reasons'] as $r) { ?>
    <p><?php echo($r); ?></p>
    <?php } ?>
  </div>
<?php } ?>
  </div>
</div>

<script>
(function($) {

  /*************************************
   *  FOR VOTING ON GOOD CAUSES BY CLICKING THE TITLE
   */ 
  $('.good-cause-link').click(function() {
    var self = $(this);    
    var id = self.data("goodCauseId");
    var name = self.data("goodCauseName");
    var url = self.data("goodCauseUrl");
    console.log(id);
    console.log(name);
    console.log(url);
    $.cookie("Drupal.visitor.goodcauseid",id);
    $.cookie("Drupal.visitor.goodcausename",name);
    $.cookie("Drupal.visitor.goodcauseurl",url);
  });

  /*************************************
   *  FOR SEARCHING GOOD CAUSES
   */
  var goodCauses = $('.good-cause-name'); 
  $('#search-good-cause').keyup(function() {
    var query = $(this).val();
    goodCauses.each(function() {
      var self = $(this);
      var parent = self.parent();
      if(query == "") {
        parent.show(); 
      } else {
        if(self.text().toLowerCase().indexOf(query.toLowerCase()) == -1) {
          parent.hide();
        } else {
          parent.show();
        }
      }
    });
  });
})(jQuery);
</script>
