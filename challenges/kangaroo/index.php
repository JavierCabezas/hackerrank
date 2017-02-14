<?php
/**
 * https://www.hackerrank.com/challenges/kangaroo
 * Created by PhpStorm.
 * User: javier
 * Date: 2/14/17
 * Time: 8:25 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d %d %d",$x1,$v1,$x2,$v2);

$x1 = intval($x1);
$v1 = intval($v2);
$x2 = intval($x2);
$v2 = intval($v2);

//Discard those cases that its obvious that one kangaroo won't catch the other one
if( ($x1 > $x2 && $v1 > $v2) || ($x1 < $x2 && $v1 < $v2) ){
    echo "NO";
    return;
}

/**
 * Returns true if the sign of the parameters given by argument are of diferent signs.
 * @param $old_dif
 * @param $new_dif
 * @return bool
 */
function has_sign_changed($old_dif, $new_dif){
    return $old_dif * $new_dif < 0;
}

//We get the distance between both kangaroos
$dif = $x1 - $x2;
/*
 * And then we do an infinite loop for each jump that will end if:
 *  1) The sign of the $dif changes (meaning that one kangaroo passed the other one). In this case we print NO.
 *  2) If $dif is zero then both kangaroos are at the same place and we print YES.
 */
while(1){
    $x1 += $v1;
    $x2 += $v2;

    $old_dif = $dif;
    $dif = $x1 - $x2;
    if($dif == 0){
        echo "YES";
        return;
    }else{
        if(has_sign_changed($old_dif, $dif)){
            echo "NO";
            return;
        }
    }
}
