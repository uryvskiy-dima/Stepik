<?php
function the_biggest_symbol($str) {
    $max = ord($str[0]);
    for ($i = 0; $i < strlen($str); $i++)
        if ($max < ord($str[$i]))
            $max = ord($str[$i]);
    return chr($max);
}

function the_sum_of_each_character($str) {
    $sum = 0;
    for ($i = 0; $i < strlen($str); $i++)
        $sum += ord($str[$i]);
    return $sum;
}

fscanf(STDIN, "%s", $str);
echo the_biggest_symbol($str) . " " . the_sum_of_each_character($str);