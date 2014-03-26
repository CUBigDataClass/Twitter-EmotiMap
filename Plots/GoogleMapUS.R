
##############################################################################
Sys.setenv(NOAWT = 1)
library(OpenStreetMap)
library(rgdal)
library(stringr)
library(ggplot2)
library(ggmap)
library(maps)
library(scales)
library(RgoogleMaps)
#Set Working Directory
setwd("~/Desktop/Twitter-EmotiMap/DataGen")

#Get geo location of tweets and the percent of literacy of the tweets
LatLong <- read.csv("LatLong.csv")
PercentLit <- read.csv("PercentLit.csv")

#Create data frame for all geo location of all tweets with literacy score
geoFrame <- data.frame(Lat = LatLong[2], Long = LatLong[1], PercLit = PercentLit[1])
#Label the Columns of the geoFrame for easy calling into that data frame
names(geoFrame)[1] <- "Lat"
names(geoFrame)[2] <- "Long"
names(geoFrame)[3] <- "Perclit"


MapUS <- get_map(location = 'united states', zoom = 4)

GoogleMapUS <- ggmap(MapUS) + geom_point(data = geoFrame, aes(x = Long, y = Lat, size = Perclit, color = Perclit)) +
      scale_size_continuous(range = c(.01, 1)) + theme(axis.line = element_blank(), axis.text.x = element_blank(),
      axis.text.y = element_blank(), axis.ticks = element_blank(),
      axis.title.x = element_blank(), axis.title.y = element_blank())+scale_colour_gradient(low="black", high="red")

GoogleMapUS


p <- sort(geoFrame$Perclit, decreasing = FALSE)

hist(p)



ggplot(data = geoFrame) + geom_
png("US_Literacy.png", 811, 588)
ggsave("US_Literacy.png", dpi=300)
########################################################################




