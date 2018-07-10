#!/bin/sh
n=$(wc -l < $1)
#echo $n
t=`expr $n - 3`
#echo $t

star=$(head -3 $1 | grep -i "the" | wc -l)
diamond=$(tail -n -$t $1 | grep -i "for" | wc -l)
#echo $star
#echo $diamond
#for((i=1 ; i<=$n ; i++))
#do
#if [ $i -le 3 ]
#then
sed -i '1,3 s/the/it/g' $1
sed -i '4,$ s/for/when/g' $1

sort -r $1
#fi
#done

cost=`expr $star \* $star + $diamond`

#cat $1
echo "cost = $cost"
