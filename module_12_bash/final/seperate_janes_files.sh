#!/bin/bash
> oldFiles.txt


        for files in /home/student/data/jane_*;do
            if test -e "$files";then echo "File exists";
            # this -e flag for parameter of file name 
            else echo "Files doesn't exist"; 
            fi 
            echo "$files" >> oldFiles.txt

        done 


