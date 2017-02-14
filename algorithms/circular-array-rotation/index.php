<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/13/17
 * Time: 9:09 PM
 */

$out = [];
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d %d",$n,$k,$q);
$a_temp = fgets($handle);
$a = explode(" ",$a_temp);
array_walk($a,'intval');

//Rotate the array
for($i = 0 ; $i < $k ; $i++){
    //We make a copy of a on a temporal array
    $clone = $a;
    $a = [];
    //Then we fill the new a array with the value of each element in the key +1 modulo array lenght.
    //By using this algorithm the last value will go to the first position (by having 0 as an index) and everything else will go foward 1 position.
    foreach($clone as $key => $value){
        $a[ ($key + 1)% $n ] = $value;
    }
    //Finally we call ksort so they array is sorted by its keys, leaving the element with 0 as the index as the first one.
    ksort($a);
}

for($a0 = 0; $a0 < $q; $a0++){
    fscanf($handle,"%d",$m);
    //Store the elements on the array as we get them
    array_push($out, intval($a[$m]));
}

//Finally print the data
foreach($out as $temp){
    echo $temp."\n";
}


