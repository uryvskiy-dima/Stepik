<?php
$numbers = explode(" ", readline()); 
$result = array();

for ($i=0; $i < count($numbers); $i++)
   if ($numbers[$i] >= 0)
        array_push($result, $numbers[$i]);
    else
        array_push($result, $numbers[$i], 0);

foreach ($result as $value) 
    echo $value . " ";