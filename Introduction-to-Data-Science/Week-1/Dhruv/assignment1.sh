head -3 $1 | sed 's/the/it/' > output.txt
tail -4 $1 | sed 's/for/when/' >> output.txt
star=$(head -3 $1 | grep "the" | wc -l | bc)
diamond=$(tail -4 $1 | grep "for" | wc -l | bc)
cost=`echo "$star * $star + $diamond"|bc`
sort -r output.txt
echo "cost = $cost"


