n=$(wc -l < $1)
f="for"
s1=$(cat $1|grep it|wc -l)
d1=$(cat $1|grep when|wc -l)

for((i=1;i<4;i++))
do
   sed -i "${i}s/the/it/" $1
done
s2=$(cat $1|grep it|wc -l)
for((i=4;i<=$n;i++))
do
   sed -i "${i}s/for/when/" $1
done
d2=$(cat $1|grep when|wc -l)
sort -r $1
c=`expr $s2 - $s1`

c1=`expr $c \* $c` 
c2=`expr $d2 - $d1`

cost=`expr $c1 + $c2`
echo $cost
exit
