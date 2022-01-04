#!/bin/bash
echo " enter yor id  number"
read n
if (( $n => 100))
echo " you are in a room"
elif (($n < 100 && $n =>  80))
echo " you are in second room"
else
echo " you are in third room"
fi
":
