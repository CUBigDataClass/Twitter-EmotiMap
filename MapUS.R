pdf();
#######################################
Sys.setenv(NOAWT = 1)
library(OpenStreetMap)
library(rgdal)
library(stringr)
library(ggplot2)
library(ggmap)
library(maps)
library(scales)
#Set Working Directory
setwd("~/Documents/School/Computing/Twitter-EmotiMap/")

#Get geo location of tweets and the percent of literacy of the tweets
LatLong <- read.csv("LatLong.csv")
PercentLit <- read.csv("PercentLit.csv")

#Create data frame for all geo location of all tweets with literacy score
geoFrame <- data.frame(Lat = LatLong[2], Long = LatLong[1])
#Label the Columns of the geoFrame for easy calling into that data frame
names(geoFrame)[1] <- "Lat"
names(geoFrame)[2] <- "Long"

map("usa")
points(x = geoFrame$Long, y = geoFrame$Lat)
geoMerc <- as.data.frame(projectMercator(geoFrame$Lat, geoFrame$Long), drop = FALSE)




names(geoMerc)[1] <- "Lat"
names(geoMerc)[2] <- "Long"
MapUS <- openmap(c(49.345786,-124.794409), c(24.7433195,-66.9513812), type = 'stamen-watercolor')
map <- autoplot(MapUS, expand = FALSE) + geom_point(aes(x = Lat, y = Long),
                                                    data = geoMerc, color = alpha(rgb(97/255,77/255,140/255), .2), 
                                                    size = 4)+theme(axis.line = element_blank(), axis.text.x = element_blank(),
      axis.text.y = element_blank(), axis.ticks = element_blank(),
      axis.title.x = element_blank(), axis.title.y = element_blank())

map

ggsave("US_Literacy.png", dpi=600)





