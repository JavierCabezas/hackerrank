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

//Discard those cases that its obvious that one kangaroo won't catch the other one
if( ($x1 > $x2 && $v1 > $v2) || ($x1 < $x2 && $v1 < $v2) ){
    echo "NO";
    return;
}

if($v1 > $v2 && ($x2-$x1)%($v1-$v2)==0 ){
    echo "YES";
    return;
}

echo "NO";
