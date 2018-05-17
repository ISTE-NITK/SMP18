n=$(wc -l < $1)
sed -e '1,3 s/the/it/g' -e "4,$n s/for/when/g" $1|sort -r
j=$(head -3 $1|grep "the"|wc -l)
k=$(tail -4 $1|grep "for"|wc -l)
res=$((($j*$j)+$k))
echo "cost=$res"

