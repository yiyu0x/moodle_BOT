#!/bin/bash 

#report file build
echo "Runtime error" > /tmp/Runtime_error.txt
echo "------------------------------------------" >> /tmp/Runtime_error.txt
echo "Compilation_ERROR" > /tmp/Compilation_error.txt
echo "------------------------------------------" >> /tmp/Compilation_error.txt
echo "Wrong" > /tmp/Wrong.txt
echo "------------------------------------------" >> /tmp/Wrong.txt
echo "Correct" > /tmp/Correct.txt
echo "------------------------------------------" >> /tmp/Correct.txt


cd hw_repo
#remove comment (avoid encode error)
#perl -pi -e 's/[^[:ascii:]]//g' `find ./ -iname *.java`
find . -iname *.java -exec perl -pi -e 's/[^[:ascii:]]//g' '{}' \;
#read -p 'Compilation target is: ' TARGET

#setting main class file#############
TARGET=CalScore
INPUTPWD=../../input/hw1.txt
ANSPWD=../../output/hw1_ans.txt
#####################################
for i in *
do
        cd $i 
        echo -n "Judging student $i... "
        javac $TARGET.java 2> /dev/null
        if [ $? -ne 0 ]
        then
                echo Compilation error
		echo $i >> /tmp/Compilation_error.txt
        else
                java $TARGET < $INPUTPWD > output 2> /dev/null
                if [ $? -ne 0 ]
                then
                        echo Runtime error
			echo $i >> /tmp/Runtime_error.txt
                else
                        cmp output $ANSPWD > /dev/null
                        if [ $? -ne 0 ]
                        then
                                echo Wrong
				echo $i >> /tmp/Wrong.txt
                        else
                                echo Correct
				echo $i >> /tmp/Correct.txt
                        fi
                fi
        fi
        cd ..
done



cd ..
pwd
echo -e "code comparing ... "
perl moss.pl hw_repo/*/*.java

echo -e "" >> /tmp/Runtime_error.txt
echo -e "" >> /tmp/Compilation_error.txt
echo -e "" >> /tmp/Wrong.txt
echo -e "" >> /tmp/Correct.txt

cat /tmp/Runtime_error.txt /tmp/Compilation_error.txt /tmp/Wrong.txt /tmp/Correct.txt > detail.txt

