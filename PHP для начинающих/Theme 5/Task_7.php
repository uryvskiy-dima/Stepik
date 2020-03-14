<?php
fscanf(STDIN, "%d %d", $x, $n);
$val = 0;
for ($i=1; $i < $n + 1; $i++)
    $val += ($x - ($x/2))**$i;
echo $val;