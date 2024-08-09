#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        # basename home.HTM .HTM  in terminal this basename command remove this .HTM extention and return name with out extention of file 
        mv "$file" "$name.html" 
done 

# Note when ever you want to change file directory name using script first we print the line in which rename process occur like this   echo mv "$file" "$name.html"  

# ./rename.sh 
# mv about.HTM about.html
# mv home.HTM home.html
# mv index.HTM index.html
# so in this way we have confirmed that file name change correctly and no any other files is effected 

# cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head this cmd display the most repeted info from system loog file 