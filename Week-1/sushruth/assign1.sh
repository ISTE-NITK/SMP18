n=$( < "file.txt" wc -l)
star=$(head -3 file.txt|grep "the"| wc -l)
a=`expr $n - 3`
dia=$(tail -$a  file.txt| grep "for"| wc -l)
sed -i -e '1,3 s/the/it/g' file.txt | sed -i -e '4,$ s/for/when/g' file.txt
cost=`expr $star \* $star \+ $dia`
sort -r file.txt
echo "cost=$cost"

