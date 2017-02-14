<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 2/13/17
 * Time: 10:52 PM
 */
$handle = fopen ("php://stdin","r");
$h_temp = fgets($handle);
$h = explode(" ",$h_temp);
array_walk($h,'intval');
fscanf($handle,"%s",$word);

