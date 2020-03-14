<?php
$str = "";
fscanf (STDIN, "%s", $str);
if (substr($str, 0, 3) == "abc")
   $str =  str_replace("abc", "www", $str, $count=1);
else 
    $str .= "zzz";
    
echo $str;
