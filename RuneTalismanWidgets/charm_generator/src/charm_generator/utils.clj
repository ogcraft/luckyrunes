(ns charm-generator.utils
  (:gen-class)
  (:require
  ;[me.raynes.conch :as sh]
  [taoensso.timbre :as log]
  [clojure.string :as s])
  (:use [clojure.java.shell]))

(def version "1.0")

(defn do-cmd [cmd args]
  (sh cmd args))

(defn size [w h]
  (format "-size %dx%d" w h))

(defn rgba [r g b a]
  (format "'rgba(%d,%d,%d,%d)'" r g b a))

(defn generate-rounded-corner-overlay [w h]
;convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,1)' -stroke "#a30000" -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" rounded_corner_overlay.png
  (let [cmd "convert"
        sz (size w h)
        fill (format "-fill %s" (rgba 255,255,255,1))
        stroke "-stroke '#a30000'"
        other "xc:none -border 3 -alpha transparent -background none"
        args (s/join " " [sz fill stroke other])
        out-fname "rounded_corner_overlay.png"]
    (printf "generate-rounded-corner-overlay: %s %s %s\n" cmd args out-fname)
    {:cmd cmd :args args :out out-fname}))

;olegg-yos:~/git/luckyrunes/RuneTalismanWidgets/ch_images1 $ python generate_charm_images.py
;Do: convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,1)' -stroke "#a30000" -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" rounded_corner_overlay.png
;Do: convert -size 320x100 xc:none -border 3 -alpha transparent -background none -fill 'rgba(255,255,255,0.3)' -stroke "#a30000" -strokewidth 4 -draw "roundRectangle 15,20 310,80 15,15" rounded_corner_overlay_transp.png
;---------------------------------
;ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png -> ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png
;Do: rm -f ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png
;Do: convert -size 320x100 xc:transparent -font runes-germanic-kern-cc-germanic-kern-cc -pointsize 50 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw "text 50,66 ',t.s.u,'" ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png
;Do: composite ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png rounded_corner_overlay.png ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png
;Do: composite ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png rounded_corner_overlay_transp.png ch0010_transp.png
;Do: composite ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png gpaper_circle_bg_shadow_320_100.png ch0010.png
;Do: rm -f ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn_script.png
;Do: convert ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate 10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn-polaroid-1.png
;Do: convert ch0010.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate 10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0010-polaroid-1.png
;Do: convert ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate -10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0010-tiwaz-sowilo-uruz-sila-energija-pobedid-bolezn-polaroid-2.png
;Do: convert ch0010.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate -10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0010-polaroid-2.png
;Do: convert -resize 72x72 -quality 100 ch0010-polaroid-1.png ch0010_icon.png
;
;---------------------------------
;ch0013-fehu-fehu-fehu_script.png -> ch0013-fehu-fehu-fehu.png
;Do: rm -f ch0013-fehu-fehu-fehu_script.png ch0013-fehu-fehu-fehu.png
;Do: convert -size 320x100 xc:transparent -font runes-germanic-kern-cc-germanic-kern-cc -pointsize 50 -channel RGBA -gaussian 0x6 -fill '#a30000' -draw "text 47,66 ',f.f.f,'" ch0013-fehu-fehu-fehu_script.png
;Do: composite ch0013-fehu-fehu-fehu_script.png rounded_corner_overlay.png ch0013-fehu-fehu-fehu.png
;Do: composite ch0013-fehu-fehu-fehu_script.png rounded_corner_overlay_transp.png ch0013_transp.png
;Do: composite ch0013-fehu-fehu-fehu_script.png gpaper_circle_bg_shadow_320_100.png ch0013.png
;Do: rm -f ch0013-fehu-fehu-fehu_script.png
;Do: convert ch0013-fehu-fehu-fehu.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate 10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0013-fehu-fehu-fehu-polaroid-1.png
;Do: convert ch0013.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate 10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0013-polaroid-1.png
;Do: convert ch0013-fehu-fehu-fehu.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate -10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0013-fehu-fehu-fehu-polaroid-2.png
;Do: convert ch0013.png -bordercolor white -border 6 -bordercolor grey60 -border 1 -background none -rotate -10 -background black \( +clone -shadow 60x4+4+4 \) +swap -background  none -flatten ch0013-polaroid-2.png
;Do: convert -resize 72x72 -quality 100 ch0013-polaroid-1.png ch0013_icon.png
;
;---------------------------------
