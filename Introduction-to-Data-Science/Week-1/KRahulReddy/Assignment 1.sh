#Calculating lines in file
len=$(cat file.txt|wc -l)

#Value of star
star=$(head -3 file.txt|grep the|wc -l)

#Value of diamond
tail_len=`expr $len - 3`
diamond=$(tail -$tail_len file.txt|grep for|wc -l)

a=$(head -3 file.txt|sed 's/the/it/g'|sort -r)

b=$(tail -$tail_len file.txt|sed 's/for/when/g'|sort -r)

#make empty file temp.txt to store edited content
>temp.txt

echo -e "$a\n$b" >> temp.txt

echo "$(cat temp.txt|sort -r)"
cost=$(expr $star \* $star + $diamond)
echo "Cost = $cost"
