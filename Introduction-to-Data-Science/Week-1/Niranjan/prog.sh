star=$(head -3 $1|grep "the"| wc -l)
n=$(grep -c ^ $1)
a=$(expr "$n" - "3")
diam=$(tail -$a $1| grep "for"| wc -l)
c=$(expr "$star" \* "$star")
c=$(expr "$c" + "$diam")
sed -i -e '1,3s/the/it/g' $1
sed -i -e '4,$s/for/when/g' $1
sort -r $1
echo "$c"
