#!/bin/bash

function showall
{
	xmlstarlet sel -t -v "//catalog/*" file.xml
}

function show
{
	xmlstarlet sel -t -v "//catalog/duck[@id="$1"]" file.xml
}

function delete
{
	xmlstarlet ed -d "//catalog/duck[@id="$1"]" file.xml
}

function add
{
	echo $1
	xmlstarlet ed --omit-decl \
  -s '//catalog' -t elem -n "duck" \
  -i '//catalog/duck[@id="$1"]' -t attr -n "id" --value "$1" \
  -s '//catalog/duck[last()]' -t elem -n "material" \
  -s '//catalog/duck[last()]' -t elem -n "color" \
  -s '//catalog/duck[last()]' -t elem -n "size" \
  -s '//catalog/duck[last()]' -t elem -n "manufacturer" \
  -s '//catalog/duck[last()]' -t elem -n "price" \
  file.xml
}

while true
do
	read action
	if [[ $action == 'showall' ]];then
		showall
	elif [[ $action == 'show'* ]];then
		a=`echo $action | awk '{print $2}'`
		show $a
	elif [[ $action == 'delete'* ]];then
		a=`echo $action | awk '{print $2}'`
		delete $a
	elif [[ $action == 'add'* ]];then
		a=`echo $action | awk '{print $2}'`
		add $a
	fi
done