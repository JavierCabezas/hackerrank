<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 6/25/17
 * Time: 12:42 AM
 */

function printArray($arr){
    foreach($arr as $ar){
        echo  implode(' ', $ar)."\n";
    }
}

function  insertionSort($ar)
{
    $inserted_element_index = count($ar) - 1;
    $last_element_index = $inserted_element_index - 1;
    $element_to_insert = $ar[$inserted_element_index];

    for ($i = $last_element_index; $i >= 0; $i -= 1) {
        $ar[$i + 1] = $ar[$i];
        if ($i == 0 || $ar[$i - 1] <= $element_to_insert ){
            $ar[$i] = $element_to_insert;
            $i = 0;
        }
    }
    return $ar;
}

function sortArray($ar){
    for($i = 0 ; $i < count($ar) ; $i+= 1){
       // $ar = sortArray()
    }
  //  printArray($temp);
}

$fp = fopen("php://stdin", "r");
fscanf($fp, "%d", $m);
$ar = array();
$s=fgets($fp);
$ar = explode(" ", $s);
for($i=0;$i < count($ar);$ar[$i++]+=0);
sortArray($ar);