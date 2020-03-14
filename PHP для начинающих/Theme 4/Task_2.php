<?php
$str = "";
fscanf (STDIN, "%s", $str);
echo (strlen($str) > 10) ? substr($str, 0, 6) : str_pad($str,  12, "o"); 