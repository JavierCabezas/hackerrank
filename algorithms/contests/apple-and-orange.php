<?php
/**
 * www.hackerrank.com/challenges/apple-and-orange
 * Created by PhpStorm.
 * User: javier
 * Date: 2/13/17
 * Time: 11:36 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d",$s,$t);
fscanf($handle,"%d %d",$a,$b);
fscanf($handle,"%d %d",$m,$n);
$apple_temp = fgets($handle);
$apples = explode(" ",$apple_temp);
$orange_temp = fgets($handle);
$oranges = explode(" ",$orange_temp);

$a = intval($a);
$s = intval($s);
$t = intval($t);

function is_fruit_in_house($tree_start, $d, $s, $t){
    $fruit_position = $tree_start + $d;
    return ($fruit_position >= $s) && ($fruit_position <= $t);
}

$apples_in_house = $oranges_in_house = 0;
foreach($apples as $d_apple){
    $apples_in_house += is_fruit_in_house($a, intval($d_apple), $s, $t) ? 1 : 0;
}
foreach($oranges as $d_orange){
    $oranges_in_house += is_fruit_in_house($b, intval($d_orange), $s, $t) ? 1 : 0;
}

echo $apples_in_house."\n".$oranges_in_house;