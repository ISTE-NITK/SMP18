echo "Input:

"
cat $1

echo "

Output:

"

head -3 $1|sed 's/the/it/' > temp
tail -n +4 $1|sed 's/for/when/'>> temp
sort -r temp|cat

head -3 $1|grep "the"|wc > xxx
read slines swords scharacters sfilename < xxx 

tail -n +4 $1|grep "for"|wc > yyy
read dlines dwords dcharacters dfilename < yyy

cost=$(echo "scale=2;$slines*$slines+$dlines"|bc)
echo "

Cost=$cost"
