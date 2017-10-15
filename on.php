<?php
$file = "buttonStatus.txt";
$handle = fopen($file,'w+');
$onstring = "on";
fwrite($handle,$onstring);
fclose($handle);
?>