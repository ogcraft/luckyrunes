(defproject charm_generator "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.7.0"]
                 [com.taoensso/timbre "4.1.1"]
                 [org.clojure/tools.namespace "0.2.11"]
                 [me.raynes/conch "0.8.0"]]
  :main ^:skip-aot charm-generator.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
