<?php
$x = 0;
fscanf (STDIN, "%d", $x);
echo $x > 10 ? $x + 100 : $x - 30;