<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/15/17
 * Time: 8:55 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d",$n,$m);
$a_temp = fgets($handle);
$a = explode(" ", $a_temp);
$b_temp = fgets($handle);
$b = explode(" ", $b_temp);


function to_int($arr){
    foreach($arr as $key => $value){
        $arr[$key] = intval($value);
    }
    return $arr;
}
$a = to_int($a);
$b = to_int($b);

/**
 * Check that all the values of $a are factors of the integer $n
 * @param $a
 * @param $n
 * @return bool
 */
function check_factor_a($a, $n){
    foreach($a as $temp){
        if($n % $temp != 0){
            return false;
        }
    }
    return true;
}

/**
 * Checks that the integer $n is divisible by all the integers on the array $b
 * @param $b
 * @param $n
 * @return bool
 */
function check_factor_b($b, $n){
    foreach($b as $temp){
        if($temp % $n != 0){
            return false;
        }
    }
    return true;
}

$out = [];
$max_a = max($a);
$min_b = min($b);


for($i = $max_a ; $i <= $min_b ; $i+=1){
    if(check_factor_a($a, $i)){
        if(check_factor_b($b, $i)){
            array_push($out, $i);
        }
    }
}

echo count($out);