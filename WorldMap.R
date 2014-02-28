#This is old code
library(maps)
LatLong <- read.csv("~/Documents/School/Computing/Twitter-EmotiMap/LatLong.csv", header=F)
PercentLit <- read.csv("~/Documents/School/Computing/Twitter-EmotiMap/PercentLit.csv", header=F)
map('usa')
map('state')
points(x = LatLong$V1, y = LatLong$V2, col = rgb(runif(5),runif(5),runif(5)) , pch = 20, cex = 1.0)
 




