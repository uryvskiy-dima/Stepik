<?php
fscanf (STDIN, "%d", $n);
if (intdiv($n, 100000) + intdiv($n, 10000) % 10 + intdiv($n, 1000) % 10 == intdiv($n, 100) % 10 + intdiv($n, 10) % 10 + $n % 10) 
    echo "You have lucky tickets";
else 
    echo "You have simple tickets";
