#!/bin/sh
fname=$1
bname=${fname%.*}
convert $fname -bordercolor white  -border 6 -bordercolor grey60 -border 1 -background  none   -rotate 10 -background  black  \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten $bname-poloroid.png
