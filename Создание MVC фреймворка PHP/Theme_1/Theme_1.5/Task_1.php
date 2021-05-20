<!-- Реализуйте __call таким образом, чтобы можно было вызывать методы название которых в формате add[Число]Points()(например: add5Points(), add1Points(), add1191919Points())

Эти методы должны увеличивать свойство $points на то значение, которое содержится между add и Points в названии метода.

Также должен быть возможен вызов метода

addPoints($point)
, который должен прибавлять значение необязательного аргумента point к свойству point к свойству points. А если же $point не был передан, то должна прибавляться единица.
-->


<?php

class User
{
    private $points = 0;

    public function __call($name, $arguments)
    {
        if ($name === 'addPoints') {
            $this->points += count($arguments) == 0 ? 1 : $arguments[0];    
        } else {
            $this->points += filter_var($name, FILTER_SANITIZE_NUMBER_INT);
        }
    }

    public function getPoints()
    {
        return $this->points;
    }
}

$user = new User();
$user->addPoints();
echo $user->getPoints() . "\n";

