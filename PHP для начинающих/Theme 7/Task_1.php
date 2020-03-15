<?php
function length_of_a_right_triangle($a, $b)
{
    return sqrt($a * $a + $b * $b);
}

fscanf (STDIN, "%d %d", $a, $b);
length_of_a_right_triangle($a, $b);