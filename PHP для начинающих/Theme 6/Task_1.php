<?php
$line = stream_get_line(STDIN, 1024, PHP_EOL); 
$numbers = explode(' ', $line); 
$sum = 0;
foreach($numbers as $number)
    if ($number)
        $sum += $number;
    else
        break;
echo $sum;