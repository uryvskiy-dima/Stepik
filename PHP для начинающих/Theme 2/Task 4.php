<?php
    $x = 0;
    fscanf (STDIN, "%d", $x);
    echo $x % 10 . (int)(($x % 100) / 10) . (int)(($x % 1000) / 100) . (int)($x / 1000);
?>