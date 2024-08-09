#!/bin/bash

# in bash if e;se block we have not any expression that would be true and false. in bash if condition execute if exit status is 0 means success  
if grep "127\.0\.0\.1" /etc/hosts; then

	echo "Everything ok"

else

	echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi

# this fi means that if else block is end 


# if test -n "$PATH"; then echo "Your path is not empty"; fi   in terminal 

# if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
 