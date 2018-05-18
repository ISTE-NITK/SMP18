STAR=$(sed -n '1,3 s/the/it/p' $1|wc -l)
DIAMOND=$(sed -n '4,$ s/for/when/p' $1|wc -l)
COST=$(echo "($STAR*$STAR)+$DIAMOND"|bc)
sed '1,3 s/the/it/' $1 > newfile.txt
sed '4,$ s/for/when/' newfile.txt > f2.txt
sort -r f2.txt
echo "cost = " $COST 
