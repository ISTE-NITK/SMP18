s=$(head -3 $1|grep -c "the")
d=$(tail -n +3 $1|grep -c "for")
c=`expr $s \* $s + $d`
cat $1|sed '1,3 s/the/it/g'|sed '3,$ s/for/when/g'|sort -r
echo "cost = $c"
