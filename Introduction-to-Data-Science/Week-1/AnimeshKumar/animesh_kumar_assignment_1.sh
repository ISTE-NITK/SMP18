n=$(wc -l < $1)
star=$(head -3 $1|grep the|wc -l)
diamond=$(tail -`expr $n - 3` $1|grep "for"|wc -l)
sed -e "1,3 s/\bthe\b/it/g" -e "4,$n s/\bfor\b/when/g" $1|sort -r
cost=`expr $star \* $star + $diamond`
echo "Cost = $cost"
