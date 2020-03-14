<?php
$str = "";
fscanf (STDIN, "%s", $str);

$str = (substr($str, 0, 3) == "abc") ?  str_replace("abc", "www", $str, $count=1) : $str . "zzz"; 
echo $str;
