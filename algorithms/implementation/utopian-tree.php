<?php
/**
 * https://www.hackerrank.com/challenges/utopian-tree
 * Created by PhpStorm.
 * User: javier
 * Date: 2/18/17
 * Time: 12:33 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$t);

$measurements = [];
for($a0 = 0; $a0 < $t; $a0++){
    fscanf($handle,"%d",$n);
    array_push($measurements, intval($n) +1 );
}

/**
 * The algorithm goes like:
 *  Iteration   | Result    |   Difference  |   Algorithm
 *      1       |    0      |       0       |       -
 *      2       |    1      |       1       |      +1
 *      3       |    2      |       1       |   + 2ˆ0 - 1
 *      4       |    3      |       2       |      +1
 *      5       |    6      |       3       |   + 2ˆ2 - 1
 *      6       |    7      |       1       |      +1
 *      7       |   14      |       7       |   + 2ˆ3 - 1
 *      8       |   15      |       1       |      +1
 *      9       |   30      |      15       |   + 2ˆ4 - 1
 *     10       |   31      |       1       |      +1
 *     11       |   62      |      31       |   + 2ˆ5 - 1
 *
 * @param $iteration The iteration #
 * @return number the result
 */
function calculate_tree_lenght($iteration){
    return pow(2, intval($iteration / 2) +1 ) - 2 + ($iteration%2);
}

foreach($measurements as $m){
    echo calculate_tree_lenght($m)."\n";
}


