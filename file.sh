#!/bin/bash 
filename = "test.txt"

if [ -f  "$filename" ] ; 
then
echo "$filename is exists."
else
echo "$filename dose not exists."
fi

echo "$filename"
