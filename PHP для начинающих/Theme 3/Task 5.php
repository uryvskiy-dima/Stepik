<?php
$x = 0;
$y = 0;
fscanf (STDIN, "%d %d", $x, $y);
echo $x > $y ? $x : $y;
?>