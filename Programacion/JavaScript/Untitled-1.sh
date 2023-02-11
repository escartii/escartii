#!/bin/bash



#Alvaro Escarti

dni=$1

for num in $(seq 1 100); then
    rc=0
    echo $dni | grep -q $num || rc=1
    ((++incremento))
    echo " * | Concurrencias "{$num} is in: "$incremento""
done

exit 0
