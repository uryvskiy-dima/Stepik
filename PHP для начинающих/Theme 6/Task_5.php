<?php
$numbers = explode(" ", readline()); 

foreach (array_keys(array_count_values($numbers)) as $value)
        echo $value . " ";
