
##############################################################################
Sys.setenv(NOAWT = 1)
library(OpenStreetMap)
library(rgdal)
library(stringr)
library(ggplot2)
library(ggmap)
library(maps)
library(scales)
library(Rgooglemaps)
#Set Working Directory
setwd("~/Documents/School/Computing/Twitter-EmotiMap/DataGen")

#Get geo location of tweets and the percent of literacy of the tweets
LatLong <- read.csv("LatLong.csv")
PercentLit <- read.csv("PercentLit.csv")

#Create data frame for all geo location of all tweets with literacy score
geoFrame <- data.frame(Lat = LatLong[2], Long = LatLong[1], PercLit = PercentLit[1])
#Label the Columns of the geoFrame for easy calling into that data frame
names(geoFrame)[1] <- "Lat"
names(geoFrame)[2] <- "Long"
names(geoFrame)[3] <- "Perclit"
map("usa")
points(x = geoFrame$Long, y = geoFrame$Lat)
geoMerc <- as.data.frame(projectMercator(geoFrame$Lat, geoFrame$Long), drop = FALSE)
names(geoMerc)[1] <- "Lat"
names(geoMerc)[2] <- "Long"

geoFrame$Lat= geoMerc$Lat
geoFrame$Long = geoMerc$Long


test <- get_map(location = 'united states', zoom = 4)


ggmap(test)


MapUS <- get_map(location = 'New York City', zoom = 9)


MapUS <- openmap(c(49.345786,-124.794409), c(24.7433195,-66.9513812), type = 'stamen-watercolor')
MapUS <- openmap(c(50.0,-124.794409), c(15.0,-66.9513812), type = 'stamen-watercolor')

map <- ggmap(test) + geom_point(data = geoFrame, aes(x = Long, y = Lat, size = Perclit, color = Perclit), alpha = .5) +
  scale_size_continuous(range = c(1, 2)) + theme(axis.line = element_blank(), axis.text.x = element_blank(),
      axis.text.y = element_blank(), axis.ticks = element_blank(),
      axis.title.x = element_blank(), axis.title.y = element_blank())+scale_colour_gradient(low="white", high="black")

map

png("US_Literacy.png", 811, 588)
ggsave("US_Literacy.png", dpi=300)
########################################################################




