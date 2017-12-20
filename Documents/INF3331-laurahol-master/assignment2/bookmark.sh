#!/bin/bash
filename='/home/i-am-me/Documents/.bookmarks'

# if user specifies -a, add directory to file

if [ "$1" == "-a" ] && [ $# -eq 2 ]; then
    echo "$2|$(pwd)" >> "$filename"
    cat "$filename"
fi

# if user specifies -r, remove directory from file, delete variable
if [ "$1" == "-r" ] && [ $# -eq 2 ]; then
    #echo "READY TO DELETE"
    #sed -i "$2" "$filename"
    sed -i -e "/$2/d" $filename |  cat -s
    unset $2
fi

# give errors


if [ $# -ne 0 ]; then
    #echo "$1"
    if [ "$1" != "-r" ]; then
            #echo "first command doesn't equal -r"
            if [ "$1" != "-a" ]; then
                echo "Error: Invalid Input, first argument must be -r or -a"
            fi
    fi
fi

if [ $# -ne 0 ]; then
    if [ "$1" == "-r" ] && [ $# -lt 2 ]; then
            echo "Error: You must enter bookmark name."
    fi
fi

# read in file line by line 
while read -r line
do
    name="$line"
    #echo "Name read from file - $name"

# find variable name and value

    IFS='|' read -r -a array <<< "$name"
    #echo ${array[0]} 
    #echo ${array[1]} 

# set variable equal to value

    first=${array[0]}
    declare $first=${array[1]}
    #echo ${array[0]}
    #echo ${!array[0]}
    #echo $rerrere

done < "$filename"


