<!-- Реализуйте класс Eat, который имеет свойства type и name и позволяет получать их с помощью функций getName, getType,  
но изменять эти свойства позволяют лишь методы setName($name), setType($type). -->

<?php

class Eat
{
    private $type;
    private $name;

    public function getName()
    {
        return $this->name;
    }

    public function getType()
    {
        return $this->type;
    }

    public function setName($name)
    {
        $this->name = $name;
    }

    public function setType($type)
    {
        $this->type = $type;
    }
}
