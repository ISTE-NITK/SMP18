lines=$( < "file.txt" wc -l)
STAR=$(head -3 file.txt|grep "the"| wc -l)
q=$(expr "$lines" - "3")
DIAMOND=$(tail -$q file.txt| grep "for"| wc -l)
COST=$(expr "$STAR" \* "$STAR")
COST=$(expr "$COST" + "$DIAMOND")
sed -i -e '1,3s/the/it/g' file.txt
sed -i -e '4,$s/for/when/g' file.txt
sort -r file.txt
echo "$COST"
