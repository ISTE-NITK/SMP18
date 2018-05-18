l=$( < "file.txt" wc -l)
s=$(head -3 file.txt|grep the| wc -l)
q=$(expr "$l" - "3")
d=$(tail -$q file.txt| grep for| wc -l)

ans=$(expr "$s" \* "$s" + "$d")

sed -i -e '1,3s/the/it/g' file.txt
sed -i -e '4,$s/for/when/g' file.txt
sort -r file.txt

echo "$ans"
