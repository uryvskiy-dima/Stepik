<?php
fscanf (STDIN, "%d %d", $a, $b);

if ($a < $b)
    for ($i = $a; $i < $b; $i++)
        echo $i . " ";
else 
    echo "Сумма не существует";
