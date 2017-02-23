<?php
/**
 * https://www.hackerrank.com/challenges/strange-advertising
 * Created by PhpStorm.
 * User: javier
 * Date: 2/22/17
 * Time: 8:31 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);


$interested = 0;
$total = 5;
$old_total = 0;
for($i = 1 ; $i <= $n ; $i ++ ){
    $interested_in_for_this_loop = intval( ($total - $old_total) / 2 );
    $old_total = $total;
    $interested += $interested_in_for_this_loop;
    $total += 3* $interested_in_for_this_loop;
}

echo $interested;