lines=$( < "fil.txt" wc -l)
star=$(head -3 file.txt| grep "the"| wc -l)
n=$(expr "$lines" - "3")
diamond=$(tail -$n fil.txt| grep "for"| wc -l)
sed -i -e '1,3s/the/it/g' fil.txt
sed -i -e '4,$s/for/when/g' fil.txt
sort -r fil.txt
x=$(expr "$star" \* "$star")
cost=$(expr "$x" + "$diamond")
echo "$cost"
