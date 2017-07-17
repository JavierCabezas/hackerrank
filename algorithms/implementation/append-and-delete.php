<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/25/17
 * Time: 7:10 PM
 */
$handle = fopen ("php://stdin","r");
fscanf($handle,"%s",$s);
fscanf($handle,"%s",$t);
fscanf($handle,"%d",$k);

class WordTransform{
    private $initial_word;
    private $final_word;
    private $number_of_operations;
    private $number_of_equal_first_characters;
    private $is_solvable;

    public function __construct($s, $k) {
        $this->initial_word = $s;
        $this->final_word = $k;
        $this->calculate_number_of_equal_first_characters();
        $this->check_if_solvable();
        $this->calculate_number_of_operations();
    }

    //Fills the number_of_equal_first_characters with the number of character shared by both of the words.
    // Ex: Initial word: hackerhappy
    //     Final word: hackerrank
    //  The shared initial word is "hacker" so we get 6.
    public function calculate_number_of_equal_first_characters(){
        $counter = 0;
        for ($key=0; $key<strlen($this->initial_word); $key++) {
            if($this->initial_word[$key] == $this->final_word[$key]){
                $counter += 1;
            }else{
                $this->number_of_equal_first_characters = $counter;
                return;
            }
        }
        $this->number_of_equal_first_characters = $counter;
    }

    //Checks and fills the is_solvable variable with a boolean value depending if the problem is solvable or not.
    //The criteria for knowing if its solvable is that the non-equal characters of the second word are just lowercase chars from a to z.
    public function check_if_solvable()
    {
        for ($key = $this->number_of_equal_first_characters; $key < strlen($this->final_word); $key++) {
            if($this->final_word[$key] > 'z' || $this->final_word[$key] < 'a'){
                $this->is_solvable = false;
                return;
            }
        }

        $this->is_solvable = true;
    }

    //Gets the min number of operations needed to transform the first word into the second one.
    //In case the problem is un-solvable it sets the value as -1.
    public function calculate_number_of_operations()
    {
        if ($this->is_solvable) {
            // First step: Delete all the extra characters from
            // Ex: Initial word: hackerhappy
            //     Final word: hackerrank
            // We should delete "happy" :(, that being strlen(initial_word) - number_of_equal_characters_at_the_beggining.
            $this->number_of_operations += (strlen($this->initial_word) - $this->number_of_equal_first_characters);

            //Then we must add all extra characters
            //Using the same example we must add "rank" to "hacker"
            //So the lenght of that is strlen(final_word) - number_of_equal_characters_at_the_beggining
            $this->number_of_operations += (strlen($this->final_word) - $this->number_of_equal_first_characters);
        }else{
            $this->number_of_operations = -1;
        }
    }

    //get method
    public function get_number_of_operations(){
        return $this->number_of_operations;
    }

    //Actually gets if the problem is solvable with EXACTLY the number given by parameter.
    public function is_solvable_with($number_of_operations){
        //Case 1: Unsolvable: you can't, no mater how many operations you use.
        if($this->number_of_operations == -1){
            return false;
        }

        //Case 2: The number of operations are identical: solvable,
        if($this->number_of_operations == $number_of_operations){
                return true;
        }

        //Case 3: If you can delete the whole word and then replace it with the final word then is solvable.
        //Keep in mind that you can use extra operations by deleting an empty string, getting the same empty string.
        //This is why initial = aba, final = aba, operations >= 6 is solvable
        if($number_of_operations > (strlen($this->initial_word) + strlen($this->final_word)) )
            return true;


        //Case 4: The number of given operations is less than the number needed: unsolvable.
        if($this->number_of_operations > $number_of_operations){
            return false;
        }

        //Case 4: We use all the avaiable operations to get the words to be equal and we still have left some operations.
        //We waste those by adding any character and then deleting it.
        //As long as we have an even number of operations we can do that.
        return ($number_of_operations - $this->number_of_operations ) % 2 == 0;
    }
}

$wt = new WordTransform($s, $t);
echo $wt->is_solvable_with($k) ? "Yes" : "No";