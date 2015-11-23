(ns charm-generator.utils
  (:gen-class)
  (:require
  ;[me.raynes.conch :as sh]
  [taoensso.timbre :as log])
  (:use [clojure.java.shell]))

(def version "1.0")


(defn test []
  (sh "ls" "-aul"))
