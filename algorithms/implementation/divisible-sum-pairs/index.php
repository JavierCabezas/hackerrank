<?php
/**
 * https://www.hackerrank.com/challenges/divisible-sum-pairs
 * Created by PhpStorm.
 * User: javier
 * Date: 2/17/17
 * Time: 12:37 AM
 */

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d",$n,$k);
$a_temp = fgets($handle);
$a = array_map('intval', explode(" ",$a_temp));

$counter = 0;
foreach($a as $key_i => $first_number){
    foreach($a as $key_j => $second_number){
        if($key_i < $key_j){
            $counter += ( ($first_number + $second_number) % $k ) == 0 ? 1 : 0;
        }
    }
}

echo $counter;