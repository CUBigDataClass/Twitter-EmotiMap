import math as m

def cityGen(lat, lon): 
    cityrad = 300
    cityDict = {'New York': [40.67, -73.94 ,cityrad],
              'Los Angeles': [34.05, -118.25,cityrad],
              'Chicago': [41.8819, -87.6278,cityrad],
              'Dallas': [32.7758, -96.7967,cityrad],
              'Houston': [29.7628, -95.3831, cityrad],
              'Philadelphia': [39.95, -75.17,cityrad],
              'Washington': [38.8951, -77.0368,cityrad],
              'Miami': [25.7877, -80.2241,cityrad],
              'Atlanta':[33.7550, -84.3900,cityrad],
              'Boston':[42.3581, -71.0636,cityrad],
              'San Francisco':[37.7833, -122.4167,cityrad],
              'Phoenix': [33.4500, -112.0667,cityrad],
              'Riverside': [33.9481, -117.3961,cityrad],
              'Detroit': [42.3314, -83.0458,cityrad],
              'Seattle': [47.6097, -122.3331, cityrad],
              'Minneapolis':[44.9833, -93.2667,cityrad],
              'San Diego': [32.7150, -117.1625,cityrad],
              'Tampa': [27.9710, -82.4650,cityrad],
              'St. Louis': [38.6272, -90.1978, cityrad],
              'Baltimore': [39.2833, -76.6167,cityrad],
              'Denver': [39.7392, -104.9847,cityrad],
              'Pittsburgh':[40.4417, -80.0,cityrad],
              'Charlotte':[35.2269, -80.8433,cityrad],
              'Portland':[45.5200, -122.6819,cityrad],
              'San Antonio':[29.4167, -98.5000,cityrad],
              'Orlando':[28.4158, -81.2989,cityrad],
              'Sacramento':[38.5556,  -121.4689,cityrad],
              'Cincinnati':[39.1000,-84.5167,cityrad],
              'Cleveland':[41.4822, -81.6697,cityrad],
              'Kansas City':[39.0997, -94.5786,cityrad]
              }
              
    for city in cityDict:
        distance = LatLonDist(cityDict[city][0], cityDict[city][1], lon, lat)
        if distance <= cityDict[city][2]:
            return(city)
    return('USA')
        
            
    
def LatLonDist(lat1, lon1, lat2, lon2):
   
    #Convert latitude and longitude into radians
    la1 = m.radians(lat1)
    la2 = m.radians(lat2)
    lo1 = m.radians(lon1)
    lo2 = m.radians(lon2)
   
    #Calculate the distance between [lat1, long1] and [lat2, long2]
    dlon = abs(lo1-lo2)
    dlat = abs(la1-la2)
    a = (m.sin(dlat/2)**2) + (m.cos(la1)*m.cos(la2)*(m.sin(dlon/2)**2))
    c = 2*m.atan2(m.sqrt(a), m.sqrt(1-a))
    d = 3961*c

    return(d)