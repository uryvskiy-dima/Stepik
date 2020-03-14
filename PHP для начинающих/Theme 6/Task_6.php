<?php
$arrayOne = explode(" ", readline()); 
$arrayTwo = explode(" ", readline()); 
$result = array_filter(array_merge($arrayOne, $arrayTwo));
rsort($result);

foreach ($result as $val)
    echo $val . " ";