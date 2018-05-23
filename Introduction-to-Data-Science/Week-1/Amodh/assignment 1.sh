n=$(wc -l <$1)
n=`expr $n - 3`
star=$(head -3 $1|grep the|wc -l)
diamond=$(tail -$n $1| grep -F 'for'| wc -l)
cost=$(($star*$star +$diamond))
{ head -3 $1|sed 's/the/it/'; tail -$n $1|sed 's/for/when/' ;} | sort -r
echo cost=$cost
