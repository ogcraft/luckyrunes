#!/bin/sh

set -v 

#convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,1)' -stroke "#a30000" -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" rounded_corner_overlay.png
#convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,0.3)' -stroke "#a30000" -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" rounded_corner_overlay_transp.png
#---------------------------------
#ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png -> ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png
#rm -f ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png
#convert -size 320x100 xc:transparent -font runes-germanic-kern-cc-germanic-kern-cc -pointsize 50 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw "text 50,66 ',t.s.u,'" ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png
#composite ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png rounded_corner_overlay.png ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png
#composite ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png rounded_corner_overlay_transp.png ch0010.png
#convert ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate 10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn-polaroid-1.png
#convert ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate -10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn-polaroid-2.png
#

color="#a30000"
convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,0)' -stroke '#a30000' -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" circle.png
convert -size 320x100 xc:transparent -font runes-germanic-kern-cc-germanic-kern-cc -pointsize 50 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw "text 50,66 ',t.s.u,'" ch0010_script.png
#grungepaper6_320_100.jpg
composite ch0010_script.png circle.png ch0010_circled.png
composite ch0010_circled.png grungepaper6_320_100.jpg ch0010.png

