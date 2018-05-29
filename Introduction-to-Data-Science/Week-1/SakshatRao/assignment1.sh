star=$(head -3 $1|grep -c 'the')
diamond=$(tail +4 $1|grep -c 'for')
cost=$(echo "scale=1; $star*$star+$diamond"|bc)
(head -3 $1|sed 's/the/it/'; tail +4 $1|sed 's/for/when/')|sort -r
echo "cost = $cost"
