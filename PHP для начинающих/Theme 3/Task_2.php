<?php
$x = 0;
fscanf (STDIN, "%d", $x);
echo $x % 2 == 0 ? $x / 2 : $x * 3;
