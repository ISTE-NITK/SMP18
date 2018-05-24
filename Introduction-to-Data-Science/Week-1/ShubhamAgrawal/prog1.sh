#!/bin/sh

lines=$( <"assgn.txt" wc -l)
star=$(head -3 assgn.txt|grep "the"| wc -l)
temp=$(expr "$lines" - "3")
diamond=$(tail -$temp assgn.txt|grep "for"| wc -l)

cost=$(expr "$star" \* "$star")
cost1=$(expr "$cost" + "$diamond")
sed -i -e '1,3s/the/it/g' assgn.txt
sed -i -e '4,$s/for/when/g' assgn.txt
sort -r assgn.txt
echo "COST= $cost1"



