
##############################################################################
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

state_data <- map_data("state")
stateMerc <- as.data.frame(projectMercator(state_data$lat, state_data$long), drop = FALSE)
names(stateMerc)[1] <- "lat"
names(stateMerc)[2] <- "long"
state_data$lat = stateMerc$lat
state_data$long = stateMerc$long


p <- autoplot(mp,expand=FALSE) + geom_polygon(aes(x=x,y=y,group=group),
                                              data=states_map_merc,fill="black",colour="black",alpha=.1) + theme_bw()
print(p)
p <- autoplot(mp_bing) + geom_map(aes(x=-10000000,y=4000000,map_id=state,fill=Murder),
                                  data=crimes,map=states_map_merc)
print(p)

MapUS <- openmap(c(49.345786,-124.794409), c(24.7433195,-66.9513812), type = 'stamen-watercolor')
MapUS_bing <- openmap(c(49.345786,-124.794409), c(24.7433195,-66.9513812), type = 'bing')


states <- autoplot(MapUS, expand = FALSE) + geom_polygon(data = state_data, aes(x = lat, y = long, group = group),
                                                         fill = "black", color = "black", alpha = .2)+ theme_bw()

  states
  
  map <- autoplot(MapUS, expand = FALSE) + geom_point(aes(x = Lat, y = Long, color = Perclit),
                                                    data = geoFrame, size = 2)+#, color = alpha(rgb(97/255,77/255,140/255)),  
                                                    
            theme(axis.line = element_blank(), axis.text.x = element_blank(),
      axis.text.y = element_blank(), axis.ticks = element_blank(),
      axis.title.x = element_blank(), axis.title.y = element_blank())+scale_colour_gradient(low="blue", high="red")

map

ggsave("US_Literacy_BAYR_trans_5.png", dpi=600)
########################################################################




