<?php
$x = 0;
fscanf (STDIN, "%d", $x);
if ($x > 10 && $x < 30)
    echo 0;
elseif  ($x < 50)
    echo $x * $x;
else
    echo "Ошибка";
