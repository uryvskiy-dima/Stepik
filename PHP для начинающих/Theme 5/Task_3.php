<?php
fscanf (STDIN, "%d %d", $a, $b);
$sum = 0;
for ($i = $a; $i < $b; $i++)
    $sum += $i;
echo $sum;

