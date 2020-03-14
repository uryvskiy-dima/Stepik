<?php
$line = stream_get_line(STDIN, 1024, PHP_EOL); 
$numbers = explode(' ', $line); 
$min = min($numbers);
$max = max($numbers);

if (count($numbers) > 1)
{
    if ($max != $min)
    {
        $posMin = array_search($min, $numbers);
        $posMax = 0;
        
        for ($i=0; $i < count($numbers); $i++)
           if ($numbers[$i] >= $max)
                $posMax = $i;
  
        $numbers[$posMin] = $max;
        $numbers[$posMax] = $min;
        
        foreach($numbers as $value)
           echo $value . " ";
    }
    else
        echo 'everyone is equal';
}
else
    echo $numbers[0];
