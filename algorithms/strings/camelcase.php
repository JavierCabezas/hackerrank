<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/13/17
 * Time: 11:22 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%s",$s);

const FIRST_UPPERCASE_LETTER_ASCII = 65;
const LAST_UPPERCASE_LETTER_ASCII = 90;

$chars = str_split($s);

/**
 * Returns a boolean that indicates if the given character is an uppercase character (A, B, C, D, ... Z)
 * @param $ascii_char: The ASCII value of the charcter to compare
 * @return bool
 */
function is_uppercase($ascii_char){
    return ($ascii_char >= FIRST_UPPERCASE_LETTER_ASCII) && ($ascii_char <= LAST_UPPERCASE_LETTER_ASCII);
}

$number_of_words = 1;
foreach($chars as $char) {
    $char_in_ascii = ord($char);
    //The total number of words is 1 + # of uppercase characters.
    $number_of_words += is_uppercase($char_in_ascii) ? 1 : 0;
}

echo $number_of_words;
