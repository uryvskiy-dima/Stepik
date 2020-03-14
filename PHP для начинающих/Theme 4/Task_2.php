<?php
$str = "";
fscanf (STDIN, "%s", $str);
if (strlen($str) > 10)
    echo substr($str, 0, 6);
else 
    echo str_pad($str,  12, "o"); 