#!/bin/bash
#FC,DP

END=$1


for i in `seq $END`
do

python test.py >> results.dat

done
