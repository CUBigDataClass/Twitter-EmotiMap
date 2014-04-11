
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

revgeocode(geoFrame$Lat, geoFrame$Long)
for (i in 1:40){
  g[2] <- as.numeric(geoFrame$Lat[i])
  g[1] <- as.numeric(geoFrame$Long[i])
  adresses[i] <- revgeocode(g)
}
library(sp)
library(maps)
library(maptools)

# The single argument to this function, pointsDF, is a data.frame in which:
#   - column 1 contains the longitude in degrees (negative in the US)
#   - column 2 contains the latitude in degrees

latlong2state <- function(pointsDF) {
  # Prepare SpatialPolygons object with one SpatialPolygon
  # per state (plus DC, minus HI & AK)
  states <- map('state', fill=TRUE, col="transparent", plot=FALSE)
  IDs <- sapply(strsplit(states$names, ":"), function(x) x[1])
  states_sp <- map2SpatialPolygons(states, IDs=IDs,
                                   proj4string=CRS("+proj=longlat +datum=wgs84"))
  
  # Convert pointsDF to a SpatialPoints object 
  pointsSP <- SpatialPoints(pointsDF, 
                            proj4string=CRS("+proj=longlat +datum=wgs84"))
  
  # Use 'over' to get _indices_ of the Polygons object containing each point 
  indices <- over(pointsSP, states_sp)
  
  # Return the state names of the Polygons object containing each point
  stateNames <- sapply(states_sp@polygons, function(x) x@ID)
  stateNames[indices]
}

# Test the function using points in Wisconsin and Oregon.
testPoints <- data.frame(x = c(-90, -120), y = c(44, 44))
latlong2state(testPoints)

g <- as.numeric(geocode("Colorado"))
revgeocode(g)

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




