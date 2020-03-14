<?php
$numbers = explode(" ", readline()); 
$count_values = array_count_values($numbers);

foreach (array_keys($count_values) as $value)
    if ($count_values[$value] > 1)
        echo $value . " ";
    elseif (count($count_values) == count($numbers))
    {
        echo  'not found';
        break;
    }