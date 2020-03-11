<?php
$x = 0;
fscanf (STDIN, "%d", $x);
if ($x < 50)
    echo $x** $x;
else if ($x > 10 && $x < 30)
    echo 0;
else
    echo "Ошибка";
?>