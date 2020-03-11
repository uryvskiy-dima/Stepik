<?php
$x = 0;
fscanf (STDIN, "%d", $x);
if ($x < 3 ||  $x == 12)
    echo "Зима";
else if (3 <= $x  && $x < 6)
    echo "Весна";
else if (6 <= $x  && $x < 9)
    echo "Лето";
else if (9 <= $x  && $x < 12)
    echo "Осень";
else
    echo "Ошибка";
?>