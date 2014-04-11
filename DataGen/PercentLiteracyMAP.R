
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

datFrame <- data.frame(PercLit = PercentLit[1])
names(datFrame)[1] <- "Args"

MapUS <- get_map(location = c(lon = datFrame$Args[4], lat = datFrame$Args[3]), zoom = datFrame$Args[2])

GoogleMapUS <- ggmap(MapUS) + 
        geom_point(y = datFrame$Args[3] , x = datFrame$Args[4], size = (datFrame$Args[5])+20,color = 'purple', alpha = .3) +
        geom_text(y = datFrame$Args[3], x = datFrame$Args[4], aes(label = datFrame$Args[1]), size = 15) +
        theme(axis.line = element_blank(), axis.text.x = element_blank(),
        axis.text.y = element_blank(), axis.ticks = element_blank(),
        axis.title.x = element_blank(), axis.title.y = element_blank())

GoogleMapUS

#p <- sort(geoFrame$Perclit, decreasing = FALSE)

#hist(p)

ggsave("NewOrleans.png", dpi=300)
########################################################################




