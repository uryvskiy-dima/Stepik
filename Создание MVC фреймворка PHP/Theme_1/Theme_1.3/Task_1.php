<!-- Сделайте так, чтобы классы Project  и Task  гарантировано имели метод execute($executor), 
а метод setWork  класса employee принимал любые объекты классов, которые имеют метод execute($executor) -->

<?php

interface Executor
{
    public function execute($executor);
}

class Project implements Executor
{
    private $id;
    private $title;
    private $description;

    public function execute($executor)
    {
        
    }
}

class Task implements Executor
{
    private $id;
    private $title;
    private $description;

    public function execute($executor)
    {

    }
    
}

class Employee
{
    private $work;

    public function setWork($executable){
        $this->work = $executable;
        $this->work->execute($this);
    }
}

$employee = new Employee();
$employee->setWork(new Task());
$employee->setWork(new Project());
