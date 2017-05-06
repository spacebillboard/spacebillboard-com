#!/bin/bash

for i in *.svg; do j=`basename "$i" .svg`; inkscape -z --file="$i" --export-png="$j.png" --export-width=32 --export-height=32; echo "converted $i"; done;
