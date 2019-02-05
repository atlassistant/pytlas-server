#!/bin/bash

#echo "Which language do you wish to support? (comma separated list without spaces)"
#read languages

#for lang in $(echo $languages | sed "s/,/ /g")
#do
#    snips-nlu download $lang
#done

echo "Creating super user"
python manage.py migrate
python manage.py createsuperuser
