
<?php
$x = 0;
$y = 0;
fscanf(STDIN,"%d %d",$x, $y);
echo ($x - $y == 100 || $y - $x == 100) ? "Да" : " Нет";
