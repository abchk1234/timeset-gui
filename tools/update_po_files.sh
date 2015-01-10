#! /bin/sh
# update_po_files.sh: script to update po files
# Meant to be run from the top level of the project directory

NAME=timeset-gui

# Change to po directory
cd po

for i in *.po ; do
	msgmerge --update --no-fuzzy-matching --backup=none $i $NAME.pot
done

exit 0
