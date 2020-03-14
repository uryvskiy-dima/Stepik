<?php
$numbers = explode(" ", readline()); 

$flag = TRUE;
for ($i=0; $i < count($numbers); $i++)
    if ($numbers[$i] == $i * $i)
    {
        echo $i . " ";
        $flag = FALSE;
    }
       
if ($flag)
    echo  'not found';