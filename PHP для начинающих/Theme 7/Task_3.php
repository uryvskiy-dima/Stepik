<?php
function count_function_calls() {
    static $count;
    return $count++;
}

count_function_calls();