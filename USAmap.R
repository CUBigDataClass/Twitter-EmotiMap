library(maps)
LatLong <- read.csv("~/Documents/School/Computing/Twitter-EmotiMap/LatLong.csv", header=F)
map('world')
points(x = LatLong$V1, y = LatLong$V2, col = rgb(runif(5),runif(5),runif(5)) , pch = 20, cex = 1.0)
 




