STAR=$(head -3 $1|grep -i the|wc -l)
li=($(wc -l $1))
((li=$li - 3))
DIAMOND=$(tail -$li $1|grep -i for|wc -l)
cost=`expr $STAR \* $STAR + $DIAMOND`
head -3 $1|sed 's/the/it/g' >temp1.txt
tail -$li $1|sed 's/for/when/g' >temp2.txt
cat temp1.txt temp2.txt|sort -r
echo "cost = "$cost


