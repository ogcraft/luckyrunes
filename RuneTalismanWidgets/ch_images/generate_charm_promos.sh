#/bin/sh
set -x
convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 200 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 50,350 '\'',f.f.f,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0013_promo_1024x500.png

convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 170 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 30,350 '\'',a.u.J.a,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0035_promo_1024x500.png

convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 170 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 100,320 '\'',l.m.t,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0025_promo_1024x500.png

convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 170 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 110,320 '\'',t.s.u,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0010_promo_1024x500.png

convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 170 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 110,320 '\'',w.u.w,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0015_promo_1024x500.png

convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 170 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 140,320 '\'',d.b.N,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0018_promo_1024x500.png

convert -size 1024x500 xc:transparent -font runesgermanickerncc -pointsize 170 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw 'text 140,320 '\'',z.r.z,'\''' aaa.png && composite aaa.png grungepaper6_promo_bg_1024x500.jpg ch0038_promo_1024x500.png


