<?php
$x = 0;
fscanf (STDIN, "%d", $x);
echo (int)($x / 100) + (int)(($x % 100) / 10) + $x % 10 ;
?>