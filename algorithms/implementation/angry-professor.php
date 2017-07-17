<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/23/17
 * Time: 8:53 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$t);

for($a0 = 0; $a0 < $t; $a0++) {
    fscanf($handle, "%d %d", $n, $k);
    $a_temp = fgets($handle);
    $a = array_map('intval', explode(" ", $a_temp));
    $c = new Classroom($n, $k, $a);
    echo $c->isProfessorHappy() ? 'YES':'NO';
    if($a0 != $t -1 ){
        echo "\n";
    }
}

class Classroom{
    private $number_of_students;
    private $min_number_of_students;
    private $attendance;

    public function __construct($n, $k, $a) {
        $this->number_of_students = $n;
        $this->min_number_of_students = $k;
        $this->attendance = $a;
    }

    function getAttendingStudents() {
        $i = 0;
        foreach ($this->attendance as $x){
            $i += $x < 1 ? 1 : 0;
        }
        return $i;
    }

    function isProfessorHappy(){
        return $this->min_number_of_students > $this->getAttendingStudents();
    }

}


