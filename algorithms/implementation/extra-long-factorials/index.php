<?php
/**
 * https://www.hackerrank.com/challenges/extra-long-factorials
 * Created by PhpStorm.
 * User: javier
 * Date: 2/14/17
 * Time: 9:59 PM
 */

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);

$total = 1;
//Note: This solution works if you have bcmul installed. I don't know if its possible to actually solve this exersice in hackkerrank by using php.
for($i = 1 ; $i <= $n ; $i++){
    $total = bcmul($total, $i);
}
echo $total;