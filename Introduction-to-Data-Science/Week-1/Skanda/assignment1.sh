


sl=$(sed -n '1,3 s/the/it/p' $1 | wc -l)
dl=$(sed -n '4,$ s/for/when/p' $1 | wc -l)
sed '1,3 s/the/it/g' $1 | sed '4,$ s/for/when/g' | sort -r 
#echo "$sl"
#echo "$dl"
cost=$((`expr $sl\*$sl+$dl`))
echo "cost=$cost"



 

