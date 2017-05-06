<ol>
<?php
module_load_include('inc.php', 'sbbcompanies', 'classes/CompanyHelperFunctions');
$urls = CompanyHelperFunctions::allCompanyURLs();
foreach($urls as $url) { 
  echo("  <li><a href=\"$url\">$url</a></li>");
}
?>
</ol>
