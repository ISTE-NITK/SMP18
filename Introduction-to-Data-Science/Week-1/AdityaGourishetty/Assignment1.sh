read fname
STAR=$(head -3 $fname|grep the|wc -l)
DIAMOND=$(tail -n+4 $fname|grep -e for|wc -l)
cost=`expr \( $STAR \* $STAR \) + $DIAMOND`
sed -e '4,$s/for/when/g' -e '1,3s/the/it/g' $fname|sort -r
echo "cost = $cost"
