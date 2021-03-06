#!python

import os
import sys

do_just_print = 1

def mysystem(s):
    print "Do:",s
    if do_just_print == 0 :
        os.system(s)

#text_font=runes-germanic-mono-cc-germanic-mono-cc
font = "runes-germanic-kern-cc-germanic-kern-cc"
size = "320x100"
color = "#a30000"
pointsize = 50
fbg = 'rounded_corner_overlay.png'
fbg_transp = 'rounded_corner_overlay_transp.png'

draw_data = [
( 10, 'tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn',                     '50,66', ',t.s.u,' ),
( 13, 'fehu-fehu-fehu',                                                     '47,66', ',f.f.f,' ),
( 15, 'wunjo-uruz-wunjo-povyshenie-zenskoj-privlekatelnosty',               '57,66', ',w.u.w,' ),
( 16, 'kenaz-uruz-ingwaz-zdorovje-ukreplenie',                              '55,66', ',k.u.N,' ),
( 17, 'kenaz-ingwaz-tiwaz-new-business-development',                        '50,66', ',k.N.t,' ),
( 18, 'dagaz-berkano-ingwaz-lechenie-besplodija',                           '53,66', ',d.b.N,' ),
( 19, 'algiz-ehwaz-dagaz-isa-pobedit-sushestvujushie-bolezni',              '43,66', 'z.e.d.i' ),
( 21, 'algiz-fehu-othala-algiz-uspeh-zaschita-deneg-buseness',              '33,66', 'z.f.o.z'),
( 22, 'algiz-laguz-berkano-sowilo-ukrepljaet-pri-psihologicheskih-problemah', '53,66', 'z.l.b.s'),
( 23, 'dagaz-othala-gebo-dolgoletie-sily-finansovyj-uspeh',                 '53,66', ',d.o.g,'),
#( 24, 'posoh-bragi-uspeshnie-ekzameny-ot-zigwult',                          '53,66', ''),
( 25, 'laguz-mannaz-tiwaz-pobeda-v-igrah',                                  '53,66', ',l.m.t,'),
( 26, 'laguz-algiz-gebo-chistaja-udacha',                                   '53,66', ',l.z.g,'),
( 27, 'algiz-laguz-berkano-sowilo-preodolenie-psihologicheskih-problem',    '47,66', 'z.l.b.s'),
( 28, 'kenaz-dagaz-fehu-poiski-raboty',                                     '53,66', ',k.d.f,' ),
( 29, 'ansuz-jera-mannaz',                                                  '53,66', ',a.j.m,'),
( 30, 'dagaz-fehu-ingwaz-othala',                                           '53,66', 'd.f.N.o'),
( 31, 'isa-kenaz-hagalaz-kenaz-isa',                                        '33,66', 'i.k.h.k.i'),
( 32, 'kenaz-gebo-wunjo-ukreplenie-lubovnyh-otnoshenij',                    '53,66', ',k.g.w,'),
( 33, 'ansuz-wunjo-tiwaz-uspeh-v-testah',                                   '53,66', ',a.w.t,'),
( 34, 'mannaz-jera-fehu-okonchanie-kursov-i-poluchenie-raboty',             '53,66', ',m.J.f,'),
( 35, 'ansuz-uruz-jera-ansuz-AUJA-privlekaet-uspeh',                        '53,66', 'a.u.J.a' ),
( 36, 'tiwaz-algiz-othala-algiz-tiwaz-zaschita-doma',                       '23,66', '.tzozt.'),
]

#font=runes-germanic-kern-cc-germanic-kern-cc
#name=ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn
#fscript=${name}_script.png
#fout=${name}.png
#rm -f $fin $fout
#convert -size 320x100 xc:transparent -font $font -pointsize 50 -channel RGBA -gaussian 0x6 -fill '#a30000' \
# -draw "text 35,66 ',tsu,'" $fscript
#composite $fscript bg.png $fout

#create background
bg_cmd = "convert -size %s xc:none -border 3 -alpha transparent -background none -fill \'rgba(255,255,255,1)\' -stroke \"%s\" -strokewidth 4 -draw \"roundRectangle 15,20 310,80 15,15\" %s" % (size, color, fbg)
mysystem(bg_cmd)
# generate fully transparent rounded_corner_overlay_transp_0.png
#convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,0)' -stroke "#a30000" -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" rounded_corner_overlay_transp_0.png
#composite rounded_corner_overlay_transp_0.png gpaper_bg_320_100.jpg gpaper_circle_bg_320_100.png

gpaper_circle_bg = "gpaper_circle_bg_shadow_320_100.png"

bg_cmd_transp = "convert -size %s xc:none -border 3 -alpha transparent -background none -fill \'rgba(255,255,255,0.3)\' -stroke \"%s\" -strokewidth 4 -draw \"roundRectangle 15,20 310,80 15,15\" %s" % (size, color,fbg_transp)
mysystem(bg_cmd_transp)

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for d in draw_data:
    print "---------------------------------"
    fname = "ch00%.2d-%s" % (d[0],d[1])
    fscript = fname + "_script.png"
    fout = fname + ".png"
    print "%s -> %s" % (fscript, fout)
    #remove previous files if exists
    rm_cmd = "rm -f %s %s" % (fscript, fout)
    mysystem(rm_cmd)
    convert_cmd = "convert -size %s xc:transparent -font %s -pointsize %d -channel RGBA -gaussian 0x6 -fill '%s' -draw \"text %s '%s'\" %s" % (size,font,pointsize,color,d[2],d[3], fscript) 
    mysystem(convert_cmd)
    composite_cmd = "composite %s %s %s" % (fscript, fbg, fout)
    mysystem(composite_cmd)
    # make transparent
    composite_cmd = "composite %s %s %s" % (fscript, fbg_transp, fout[:6]+"_transp.png")
    mysystem(composite_cmd)
    # make with paper bg
    fout_gpaper =  fout[:6]+".png"
    composite_cmd = "composite %s %s %s" % (fscript, gpaper_circle_bg, fout_gpaper)
    mysystem(composite_cmd)
    mysystem("rm -f %s" % fscript)
    # generate polaroid
    rotate = 10
#convert %s -bordercolor white  -border 6 -bordercolor grey60 -border 1 -background  none -rotate 10 -background  black  \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten $bname-poloroid.png
    polar_cmd="convert %s -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate %d -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten %s" % (fout, (rotate),fout[:-4] + "-polaroid-1.png") 
    mysystem(polar_cmd) 
    polar_cmd="convert %s -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate %d -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten %s" % (fout_gpaper, (rotate),fout_gpaper[:-4] + "-polaroid-1.png") 
    mysystem(polar_cmd) 
    polar_cmd="convert %s -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate %d -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten %s" % (fout, (-rotate),fout[:-4] + "-polaroid-2.png")  
    mysystem(polar_cmd) 
    polar_cmd="convert %s -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate %d -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten %s" % (fout_gpaper, (-rotate),fout_gpaper[:-4] + "-polaroid-2.png")  
    mysystem(polar_cmd) 
    icon_cmd="convert -resize 72x72 -quality 100 %s-polaroid-1.png %s_icon.png" % (fout_gpaper[:-4], fout_gpaper[:-4])
    mysystem(icon_cmd) 
    print


