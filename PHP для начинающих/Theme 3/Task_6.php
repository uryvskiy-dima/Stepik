<?php
$x = 0;
$y = 0;
fscanf(STDIN,"%d %d",$x, $y);
echo abs($x - $y) <= 20 ? "Да" : "Нет";
