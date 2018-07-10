STAR=$(head -3 $1 | grep -c the)
DIAMOND=$(tail -n +4 $1 | grep -c for) 
s=$(echo "$STAR*$STAR+$DIAMOND" | bc)
head -3 $1 | sed 's/the/it/g' > temp1.txt
tail -n +4 $1 | sed 's/for/when/g' > temp2.txt
cat temp1.txt temp2.txt | sort -r > $1
cat $1
echo "Cost=$s"
rm temp1.txt temp2.txt
