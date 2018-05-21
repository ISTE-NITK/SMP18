lines=$(wc -l $1|cut -f1 -d' ')
star=$(head -3 $1|grep 'the'|wc -l|cut -f1 -d' ')
remLines=$(echo `expr $lines - 3`)
diamond=$(tail -$remLines $1|grep 'for'|wc -l)
head -3 $1|sed 's/the/it/' > 'top.txt'
tail -$remLines $1|sed 's/for/when/' > 'bottom.txt'
cost=$(echo "$star * $star + $diamond"|bc)
cat top.txt bottom.txt | sort -r
echo "cost = $cost"
rm top.txt bottom.txt
