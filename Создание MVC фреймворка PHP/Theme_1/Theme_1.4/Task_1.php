<!-- Реализуйте любой класс со статическим public свойством $count, которое инкрементируется при создании новых объектов этого класса. -->


<?php

class Example 
{
    public static $count;

    function __construct()
    {
        self::$count++;
    }
}