
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


PercentLit <- read.csv("PercentLit.csv")

geoFrame <- data.frame(PercLit = PercentLit[1])

names(geoFrame)[1] <- "PercLit"

MapUS <- get_map(location = 'united states', zoom = 4)

GoogleMapUS <- ggmap(MapUS) + 
        geom_point(y = 40.6700, x = -73.94, size = 100,color = 'red', alpha = .3) +
        geom_text(y = 40.6700, x = -73.94, aes(label = geoFrame$PercLit), size = 15) +
        theme(axis.line = element_blank(), axis.text.x = element_blank(),
        axis.text.y = element_blank(), axis.ticks = element_blank(),
        axis.title.x = element_blank(), axis.title.y = element_blank())

GoogleMapUS

#p <- sort(geoFrame$Perclit, decreasing = FALSE)

#hist(p)

ggsave("US_Literacy.png", dpi=300)
########################################################################




