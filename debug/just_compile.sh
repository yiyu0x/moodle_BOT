#!/bin/bash
cd hw_repo
perl -pi -e 's/[^[:ascii:]]//g' `find . -iname *.java`
read -p 'Compilation target is(main class file without .java): ' TARGET
for i in *
do
        cd $i
        echo -n "Judging student $i... "
        javac $TARGET.java > /dev/null
        if [ $? -ne 0 ]
        then
                echo 'Compilation error'
        else
                echo 'Compilation success'
        fi
        cd ..
done
