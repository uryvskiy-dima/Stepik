<?php
fscanf(STDIN, "%d", $value);
$a = $value % 10;
$b = $value / 10 % 10;
$c = $value / 100 % 10;
echo max($a, $b, $c), ($a + $b + $c) - max($a, $b, $c) - min($a, $b, $c), min($a, $b, $c);

