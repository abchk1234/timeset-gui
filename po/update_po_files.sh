#! /bin/sh
# update_po_files.sh: script to update po files

NAME=timeset

for i in *.po ; do
	msgmerge --update --no-fuzzy-matching --backup=none $i $NAME.pot
done
