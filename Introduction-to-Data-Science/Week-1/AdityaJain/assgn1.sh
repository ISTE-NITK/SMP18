#!/bin/bash

#counting the number of star lines and diamond lines
STLINES=$(head -3 $1|grep -wc "the")
DILINES=$(tail -n +4 $1|grep -wc "for")

#calculating cost
COST=$(($STLINES*$STLINES+$DILINES))

#editing the file
sed -i -e '1,3{s/\<the\>/it/g}' -e '4,${s/\<for\>/when/g}' $1

#printing in reverse sorted order and printing the cost
sort -r $1
echo $COST
