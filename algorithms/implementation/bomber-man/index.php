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
        $matrix[$row][$column] = $complete_row[$column] == '.' ? -1 : intval($complete_row[$column]);
    }
}

/**
$matrix = [
    [ -1,-1,-1,-1,-1,-1,-1 ],
    [ -1,-1,-1,0,-1,-1,-1 ],
    [ -1,-1,-1,-1,0,-1,-1 ],
    [ -1,-1,-1,-1,-1,-1,-1 ],
    [ 0,0,-1,-1,-1,-1,-1 ],
    [ 0,0,-1,-1,-1,-1,-1 ]
];
 * */

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
            echo $data == -1 ? '.':$data;
        }
//        echo "<br>";
        echo "\n";
    }
}


/**
 * Fields can have 5 states:
 *      1)  . : Empty field. Bombs can be placed here.
 *      2)  0 : Newly placed bombs.
 *      3)  1 : Bombs after t=1
 *      4)  2 : Bombs about to explode.
 *      5)  3 : Bombs exploding.
 *
 * @param $matrix
 * @param $is_bomberman_going_to_put_bombs: Boolean value indicating if bomberman is resting or not.
 */
function loop($matrix, $is_bomberman_going_to_put_bombs){
    foreach($matrix as $key_row => $row){
        foreach($row as $key_column => $data){
            switch($data){
                case -1:
                    if($is_bomberman_going_to_put_bombs){
                        $matrix[$key_row][$key_column] = 0;
                    }
                    break;
                case 0:
                case 1:
                case 2:
                    $matrix[$key_row][$key_column] += 1;
                    break;
                case 3:
                    $matrix[$key_row][$key_column] = -1;
                    break;
            }
        }
    }
    return $matrix;
}

print_matrix($matrix);
$matrix = loop($matrix, false);

echo "\n";
print_matrix($matrix);
$matrix = loop($matrix, true);

echo "\n";
print_matrix($matrix);
$matrix = loop($matrix, false);

echo "\n";
print_matrix($matrix);
$matrix = loop($matrix, true);

echo "\n";
print_matrix($matrix);
$matrix = loop($matrix, false);

