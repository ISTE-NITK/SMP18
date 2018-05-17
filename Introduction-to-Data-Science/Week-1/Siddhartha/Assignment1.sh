star=$(head -3 $1|grep -c "the")
dia=$(tail -n +3 $1|grep -c "for")
cat $1|sed '1,3 s/the/it/g'|sed '3,$ s/for/when/g'|sort -r
cost=$(echo "$star * $star + $dia"|bc)
echo "cost = $cost"
