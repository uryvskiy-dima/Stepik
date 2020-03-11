<?php
$a = 8;
$b = 4;
$c = 2;
fscanf(STDIN, "%d %d %d", $a, $b, $c);
echo ($a + $b) / $c . " " . ($a + $c) / $b . " " . ($b + $c) / $a;
?>