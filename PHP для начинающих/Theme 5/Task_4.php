<?php
fscanf (STDIN, "%d %d", $n, $m);

for ($i = 0; $i < 1000; $i++)
    if ($i % $m == 0 and substr_count($i, $n))
        echo $i . " ";
