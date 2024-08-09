#!/bin/bash

n=0
command=$1
# this $1 is command line first argument in this code this is return random value from ramdom_exit.py 
while ! $command && [ $n -le 5 ]; do
# this condition means if random value e.g exit status  is not 0 means first condition is true and other consition initailly obvious true so T T body execute untill 5 time execution complete or exit status is 0 
        sleep $n
        # reason for sleep is waiting may this connection is not lost due to some cpu or network overloading so it should be wait for some time
        ((n+=1))
        echo "Retry #$n"
done;

# this while body is end with done; statement 