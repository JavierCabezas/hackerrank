<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/13/17
 * Time: 10:52 PM
 */
const FIRST_LOWERCASE_LETTER_ASCII = 97;

$handle = fopen ("php://stdin","r");
$h_temp = fgets($handle);
$h = explode(" ",$h_temp);
array_walk($h,'intval');
fscanf($handle,"%s",$word);

$chars = str_split($word);
$max_index = 0;

foreach($chars as $char){
    //Get the index of the h array by ASCII value of the input and lowering it by the position of lowercase a on the table.
    $index = ord($char) - FIRST_LOWERCASE_LETTER_ASCII;

    //Update the max H value for the word in case a bigger one is found.
    if($h[$max_index] < $h[$index]){
        $max_index =  $index;
    }
}

//Return the area of the rectangle by multiplying the lenght of the string and the max. height found.
echo strlen($word) * $h[$max_index];