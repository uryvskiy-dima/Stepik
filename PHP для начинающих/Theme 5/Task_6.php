<?php
fscanf(STDIN, "%d", $n);
$sum = 0;
for ($i=0; $i < $n; $i++)
    $sum += $i * $i;
echo $sum;