<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/13/17
 * Time: 10:22 PM
 */
$_fp = fopen("php://stdin", "r");

//Scan input, We know that we are going to get exactly 5 integer.
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d %d %d %d",$a0,$a1,$a2,$a3,$a4);
$a = [$a0, $a1, $a2, $a3, $a4];

$min_index = $max_index = 0;
$sum = 0;
foreach($a as $key => $value){

    //We update both the indexes of the min and the max value
    if( $value < $a[$max_index] ){
        $max_index = $key;
    }
    if( $value > $a[$min_index] ){
        $min_index = $key;
    }

    //Store the sum of all values
    $sum += $value;
}

//Min sum: total - $a[$max_index]
//Max sum: total - $a[$min_index]
echo ($sum - $a[$min_index]).' '.($sum - $a[$max_index]);




