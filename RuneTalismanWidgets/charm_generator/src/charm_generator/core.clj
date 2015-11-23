(ns charm-generator.core
  (:gen-class)
  (:require
    [charm-generator.utils :as utils]
    [taoensso.timbre :as log]))

(defn -main
  [& args]
  (println "Starting charm-generator" utils/version)
  (println "End of charm-generator" )
  (System/exit 0))
