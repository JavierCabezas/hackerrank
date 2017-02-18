<?php
/**
 * https://www.hackerrank.com/challenges/sock-merchant
 * Created by PhpStorm.
 * User: javier
 * Date: 2/18/17
 * Time: 12:27 AM
 */

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);
$c_temp = fgets($handle);
$c = array_map('intval', explode(" ",$c_temp));

$repeats = [];
$counter = 0;
foreach($c as $elem){
    if(!isset($repeats[$elem])){
        //Initialize the counter array.
        $repeats[$elem] = 1;
    }else{
        //Add one element to the $elem index
        $repeats[$elem] += 1;
        //If the number of elements is even we have a pair and we must add one to the counter
        $counter += ( 1 - ($repeats[$elem] % 2) );
    }
}

echo $counter;