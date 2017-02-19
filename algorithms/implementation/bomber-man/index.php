<?php
/**
 * https://www.hackerrank.com/challenges/bomber-man
 * Created by PhpStorm.
 * User: javier
 * Date: 2/18/17
 * Time: 7:05 PM
 */
$_fp = fopen("php://stdin", "r");

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d %d",$r,$c,$n);

$matrix = [];
for($row = 0; $row < $r ; $row += 1){ //Read all the rows
    $complete_row = fgets($handle);
    $matrix[$row] = [];
    for($column = 0; $column < strlen($complete_row) -1 ; $column += 1) { //The -1 is because we dont want the \n character
        $matrix[$row][$column] = $complete_row[$column];
    }
}

/**
 * Prints the matrix on the CLI.
 * @param $matrix
 * Ex:
 *      .......
 *      ...O...
 *      ....O..
 *      .......
 *      OO.....
 *      OO.....
 */
function print_matrix($matrix){
    foreach($matrix as $row){
        foreach($row as $data){
            echo $data;
        }
        echo "\n";
    }
}

echo print_matrix($matrix);