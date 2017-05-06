<?php
/**
 *  SUPPORT
 */
module_load_include('inc','webform','includes/webform.submissions');
module_load_include('inc.php','sbbpersonalmsg','classes/PurchaseWebformSubmission');

/**
 *  Get the submissions
 */
$webform_submissions = webform_get_submissions(array('nid'=>variable_get('sbbpersonalmsg_purchases_webform_id')));
$submissions = array();
foreach($webform_submissions as $s) {
  $submission = new PurchaseWebformSubmission($s);
  $submissions[$submission->getId()] = $submission;
}

/**
 *  Get the submissions that have already been generated
 */
include(drupal_get_path('theme', 'sbbtheme') . '/the-billboard/generated/customers_and_personal_messages.inc.php');
$generated = array();
foreach($sbb_personal_messages as $msg) {
  array_push($generated, $msg['id']);
}

/**
 *  Get the submissions that can be generated
 */
$canBeAdded = array();
foreach($submissions as $id => $submission) {
  if(! in_array($id, $generated) && $submission->isCompleted()) {
    array_push($canBeAdded, $submission);
  }
}

/**
 *  For completeness, also collect the submissions that are not yet complete.
 */
$notCompleted = array();
foreach($submissions as $id => $submission) {
  if(! $submission->isCompleted()) {
    array_push($notCompleted, $submission);
  }
}

/**
 *  Get the submissions that can be sent
 */
$canBeSent = array();
$incomplete = array();
foreach($submissions as $id => $submission) {
  if($submission->isSent()) {
    //echo("sent");
    continue;
  }
  // not sent already, check whether it is generated
  // check two things: in data.yaml and certificates exist (just to be sure)
  if(! in_array($id, $generated)) {
    continue;
  }
  $missingFile = sbb_files_exist_for($submission);
  if($missingFile == NULL) {
    $canBeSent[$id] = $submission;
  } else {
    $incomplete[$id] = $missingFile;
  }
}

/**
 *  Send the emails for the submissions that can be sent if asked for
 */
$sendingResults = array();
if(isset($_POST['sendMails']) && $_POST['sendMails'] == true) {
  $sendingResults = sbb_send_pmsg_emails($canBeSent);
  foreach($sendingResults as $id => $result) {
    if($result == "sent") {
      unset($canBeSent[$id]);
    }
  }
}
?>

<h3>New submissions that can be added</h3>

<pre>
<?php 
foreach($canBeAdded as $submission) {
  echo($submission->toBash() . "\n");
  echo("evince ../../../../../static/valentine/valentine-" . $submission->getId() . ".pdf" . "\n");
}
echo('./build-all.py');
?>
</pre>

<h3>E-mails that can be sent</h3>

<ul>
<?php 
foreach($canBeSent as $submission) {
  $id = $submission->getId();
  echo("<li>$id</li>");
}
?>
</ul>
<?php if(count($canBeSent) > 0): ?>
<form action="/pmsg-mgmt" method="POST">
  <input type="hidden" name="sendMails" value="true">
  <input type="submit" value="Send mails" class="btn btn-warning">
</form>
<?php endif; ?>

<?php if(count($sendingResults) > 0): ?>
<h3>E-mails that were sent</h3>

<ul>
<?php 
foreach($sendingResults as $id => $result) {
  echo("<li>$id: $result</li>");
}
?>
</ul>
<?php endif; ?>

<?php if(count($incomplete) > 0): ?>
<h3>Submissions with missing files were found!!!!</h3>

<ul>
<?php 
foreach($incomplete as $id => $missing) {
  echo "<li>$id: $missing</li>";
}
?>
</ul>
<?php endif; ?>
