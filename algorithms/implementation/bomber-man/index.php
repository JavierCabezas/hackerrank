<?php
/**
 * https://www.hackerrank.com/challenges/bomber-man
 * Created by PhpStorm.
 * User: javier
 * Date: 2/18/17
 * Time: 7:05 PM
 */
class Bomberman{
    private $matrix;

    public function __construct($data) {
        $this->matrix = $data;
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
    public function print_matrix(){
        foreach($this->matrix as $cur_row => $row){
            foreach($row as $data){
                echo $data == -1 ? '.':'O';
            }
            if(count($row) -1 != $cur_row){
                echo "\n";
            }
        }
    }

    public function print_2d(){
        $matrix_arr = $this->matrix;
        $table_html = '';
        $table_html .= '<table border="-1">
                    <tr>';
        foreach ($matrix_arr as $key => $matrix_subarr) {
            $table_html .= '<tr>';
            foreach ($matrix_subarr as $value) {
                $table_html .='<td>'.$value.'</td>';
            }
            $table_html .=  '</tr>';
        }
        $table_html .= '</table>';
        echo $table_html;
    }

    function explode_bombs(){
        foreach($this->matrix as $r => $row){
            foreach($row as $c => $data){
                if($this->matrix[$r][$c] == 3){
                    $this->matrix[$r][$c] = -1;

                    if(isset($this->matrix[$r+1][$c]) && $this->matrix[$r+1][$c] != 3){
                        $this->matrix[$r+1][$c] = -1;
                    }
                    if(isset($this->matrix[$r-1][$c]) && $this->matrix[$r-1][$c] != 3){
                        $this->matrix[$r-1][$c] = -1;
                    }
                    if(isset($this->matrix[$r][$c+1]) && $this->matrix[$r][$c+1] != 3){
                        $this->matrix[$r][$c+1] = -1;
                    }
                    if(isset($this->matrix[$r][$c-1]) && $this->matrix[$r][$c-1] != 3){
                        $this->matrix[$r][$c-1] = -1;
                    }

                }
            }
        }
    }
    /**
     * Fields can have 4 states:
     *      1)  -1 : Empty field. Bombs can be placed here.
     *      2)   0 : Bombs at t=0.
     *      3)   1 : Bombs at t=1
     *      4)   2 : Bombs at t=2
     *      5)   3 : Bombs at t=3. Triggered to explode.
     *
     * @param $matrix
     * @param $is_bomberman_going_to_put_bombs: Boolean value indicating if bomberman is resting or not.
     */
    function loop($is_bomberman_going_to_put_bombs, $number_of_loops = 1){
        for($i = 0 ; $i < $number_of_loops ; $i += 1){
            foreach($this->matrix as $r => $row){
                foreach($row as $c => $data){
                    if($data == -1 && $is_bomberman_going_to_put_bombs) {
                        $this->matrix[$r][$c] = 0;
                    }else{
                        if(in_array($data, [0, 1, 2])){
                            $this->matrix[$r][$c] += 1;
                        }
                    }
                }
            }
            $this->explode_bombs();

            //Intercalate the turns in where bomberman rests and where it put bombs
            $is_bomberman_going_to_put_bombs = !$is_bomberman_going_to_put_bombs;
        }
    }
}


//Read input data
$_fp = fopen("php://stdin", "r");

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d %d",$r,$c,$n);

$matrix = [];
for($row = 0; $row < $r ; $row += 1){ //Read all the rows
    $complete_row = fgets($handle);
    $matrix[$row] = [];
    for($column = 0; $column < strlen($complete_row) ; $column += 1) { //The -1 is because we dont want the \n character
        if($complete_row[$column] != "\n"){
            $matrix[$row][$column] = $complete_row[$column] == '.' ? -1 : intval($complete_row[$column]);
        }
    }
}

$matrix = [
    [-1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1],
    [0, 0, -1, -1, -1],
    [0, 0, -1, -1, -1]
];

//Solve the problem using the class
$b = new Bomberman($matrix);

for($n = 1 ; $n < 12 ; $n++){
    switch($n) {
        //In case we get 1 we return the matrix as-is
        case 1:
            break;
        case 2:
            //In the second case bomberman was just watching without doing anything
            $b->loop(false, 1);
            break;
        case 3:
            //Third case: Bomberman watched and then filled everything with bombs.
            $b->loop(false, 2);
            break;
        default:
            //From fourth to n it follows a loop in where the bomb location repeats itself after every 4 turns.
            $case = intval($n) % 4;
            $b->loop(false, $case + 3);
            break;
    }

    $b->print_2d();
    echo "<br>";
}

