<?php
$a = 0;
$b = 0;
$c = 0;
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$D = $b * $b - (4 * $a * $c);
$x1 = (-$b + sqrt($D)) / (2 * $a);
$x2 = (-$b - sqrt($D)) / (2 * $a);
if ($D > 0)
    echo $x1 . " " . $x2;
elseif ($D == 0) 
    echo $x1;
else 
    echo "Нет ответа";