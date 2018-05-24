a=$(sed -n '1,3 s/the/it/pg' $1|wc -l)
b=$(sed -n '4,$ s/for/when/pg' $1|wc -l)
sed '1,3 s/the/it/g' $1 |sed '3,$ s/for/when/g'|sort -r 
c=`expr $a \* $a + $b`
echo "cost=$c"
