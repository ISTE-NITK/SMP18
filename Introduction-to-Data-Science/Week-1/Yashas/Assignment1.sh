STAR=$(head -3 file.txt|grep the|wc -l)
lines=$(grep -c ^ file.txt)
q=$(expr "$lines" - "3")
DIAMOND=$(tail -$q file.txt| grep "for"|wc -l)
sed -i '1,3s/the/it/g' file.txt
sed -i '4,$s/for/when/g' file.txt
sort -r file.txt
COST=$(expr $(expr $STAR \* $STAR) + $DIAMOND)
echo "$COST"
