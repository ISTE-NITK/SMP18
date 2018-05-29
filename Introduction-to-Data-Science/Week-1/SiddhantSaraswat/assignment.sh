cat $1

star1=$(sed '1!d' text.txt | grep -o 'the' | wc -l) 
star2=$(sed '2!d' text.txt | grep -o 'the' | wc -l)
star3=$(sed '3!d' text.txt | grep -o 'the' | wc -l)
STAR=`expr $star1 + $star2 + $star3`
echo 'STAR' $STAR

sed -i '1s/the/it/' $1
sed -i '2s/the/it/' $1
sed -i '3s/the/it/' $1

n=$(grep -c ^ $1)

diamond1=$(tac text.txt | sed -n 1p | grep -o 'for' | wc -l)
diamond2=$(tac text.txt | sed -n 2p | grep -o 'for' | wc -l)
diamond3=$(tac text.txt | sed -n 3p | grep -o 'for' | wc -l)
diamond4=$(tac text.txt | sed -n 4p | grep -o 'for' | wc -l)
DIAMOND=`expr $diamond1 + $diamond2 + $diamond3 + $diamond4`
echo 'DIAMOND' $DIAMOND

COST=`echo "$STAR*$STAR + $DIAMOND" | bc -l`
echo 'COST : ' $COST

#tac $1 | sed '1 s/for/when/' | tac
#tac $1 | sed '2 s/for/when/' | tac
#tac $1 | sed '3 s/for/when/' | tac
#tac $1 | sed '4 s/for/when/' | tac

sed -i '1!s/for/when/' $1
sed -i '2!s/for/when/' $1
sed -i '3!s/for/when/' $1
sed -i '4!s/for/when/' $1




