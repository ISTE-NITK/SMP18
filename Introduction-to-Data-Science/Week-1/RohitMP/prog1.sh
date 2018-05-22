
i=$(head -3 $1 | grep the -c)
j=$(tail --lines=+4 $1 | grep for -c)
s=$(echo "$i*$i+$j" | bc)
head -3 $1 | sed 's/the/it/g' > temp1.txt
tail --lines=+4 $1 | sed 's/for/when/g' > temp2.txt
cat temp1.txt temp2.txt | sort -r > $1
cat $1
echo "cost = $s"
rm temp1.txt temp2.txt


