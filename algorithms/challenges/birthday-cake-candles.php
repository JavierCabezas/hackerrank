<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 6/24/17
 * Time: 4:18 PM
 */
$handle = fopen ("php://stdin", "r");
function birthdayCakeCandles($n, $ar) {
    $max = [
        'whos_max' => 0,
        'quantity' => 0
    ];

    foreach($ar as $t){
        if($t > intval($max['whos_max'])){
            $max['whos_max'] = $t;
            $max['quantity'] = 0;
        }

        if($t == $max['whos_max']){
            $max['quantity'] += 1;
        }
    }

    return $max['quantity'];
}

fscanf($handle, "%i",$n);
$ar_temp = fgets($handle);
$ar = explode(" ",$ar_temp);
$ar = array_map('intval', $ar);
$result = birthdayCakeCandles($n, $ar);
echo $result . "\n";
