<?php
$numbers = explode(" ", readline()); 
$sum = 0;
foreach($numbers as $number)
    if ($number)
        $sum += $number;
    else
        break;
echo $sum;