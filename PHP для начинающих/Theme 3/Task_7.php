<?php
$x = 0;
fscanf (STDIN, "%d", $x);
if ($x < 3 ||  $x == 12)
    echo "Зима";
elseif  (3 <= $x  && $x < 6)
    echo "Весна";
elseif  (6 <= $x  && $x < 9)
    echo "Лето";
elseif  (9 <= $x  && $x < 12)
    echo "Осень";
else
    echo "Ошибка";
