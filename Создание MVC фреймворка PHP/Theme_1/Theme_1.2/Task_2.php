<!-- Реализовать систему классов состоящую из 3-х элементов, так чтобы третий класс наследовался от второго, а второй от первого.  

Придумать для этого логичную предметную область (например:  первый класс - Продукты ->  второй класс - Фрукты -> третий класс - Яблоко), 
так, чтобы в них логичным образом наследовались свойства, но не были доступны в объектах этих классов, сделать геттеры и сеттеры в соответствующих классах 
для доступа к этим свойствам.

Всего реализовать не менее 7 свойств в сумме во всех классах.

Конструкторы классов оставить без аргументов.

Пример системы классов (без выполнения требований): -->

<?php

class Company
{
    protected $nameCompany;
    protected $quantityDepartment;

    function __construct()
    {

    }

    public function getNameCompany()
    {
        return $this->nameCompany;
    }

    public function getQuantityDepartment()
    {
        return $this->quantityDepartment;
    }

    public function setNameCompany($nameCompany)
    {
        $this->nameCompany = $nameCompany;
    }

    public function setQuantityDepartment($quantityDepartment)
    {
        $this->quantityDepartment = $quantityDepartment;
    }
}

class Department extends Company
{
    protected $nameDepartament;
    protected $quantityWorker;

    function __construct()
    {
        
    }

    public function getNameDepartament()
    {
        return $this->nameDepartament;
    }

    public function getQuantityWorker()
    {
        return $this->quantityWorker;
    }

    public function setNameDepartament($nameDepartament)
    {
        $this->nameDepartament = $nameDepartament;
    }

    public function setQuantityWorker($quantityWorker)
    {
        $this->quantityWorker = $quantityWorker;
    }
}

class Worker extends Department
{
    protected $nameWorker;
    protected $ageWorker;
    protected $specialization;

    function __construct()
    {
        
    }

    public function getNameWorker()
    {
        return $this->nameWorker;
    }

    public function getAgeWorker()
    {
        return $this->ageWorker;
    }

    public function getSpecialization()
    {
        return $this->specialization;
    }

    public function setNameWorker($nameWorker)
    {
        $this->nameWorker = $nameWorker;
    }

    public function setAgeWorker($ageWorker)
    {
        $this->ageWorker = $ageWorker;
    }

    public function setSpecialization($specialization)
    {
        $this->specialization = $specialization;
    }
}
