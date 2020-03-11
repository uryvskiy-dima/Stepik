<?php
fscanf(STDIN, "%d", $Ch);
$a = $Ch % 10;
$b = $Ch / 10 % 10;
$c = $Ch / 100 % 10;
echo max($a, $b, $c), ($a + $b + $c) - max($a, $b, $c) - min($a, $b, $c), min($a, $b, $c);
?>
