<?php
$file = "buttonStatus.txt";
$handle = fopen($file,'w+');
$onstring = "off";
fwrite($handle,$onstring);
fclose($handle);
?>