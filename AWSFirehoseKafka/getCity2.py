#!/usr/bin/python
import math

def getCity(lat,long):

    radiusEarth = 3960
    cityrad = 300
    cityDict = {'New York': [40.67,-73.94,cityrad],
                'Los Angeles': [34.05, -118.25,cityrad],
                'Chicago': [41.8819, -87.6278,cityrad],
                'Dallas': [32.7758, -96.7967,cityrad],
                'Houston': [29.7628, -95.3831, cityrad],
                'Philadelphia': [39.95,-75.17,cityrad],
                'Washington': [38.8951, -77.0368,cityrad],
                'Miami': [25.7877, -80.2241,cityrad],
                'Atlanta':[33.7550, -84.3900,cityrad],
                'Boston':[42.3581,-71.0636,cityrad],
                'San Francisco':[37.7833,-122.4167,cityrad],
                'Phoenix': [33.4500,-112.0667,cityrad],
                'Riverside': [33.9481, -117.3961,cityrad],
                'Detroit': [42.3314, -83.0458,cityrad],
                'Seattle': [47.6097, -122.3331, cityrad],
                'Minneapolis':[44.9833, -93.2667,cityrad],
                'San Diego': [32.7150, -117.1625,cityrad],
                'Tampa': [27.9710, -82.4650,cityrad],
                'St. Louis': [38.6272, -90.1978, cityrad],
                'Baltimore': [39.2833, -76.6167,cityrad],
                'Denver': [39.7392, -104.9847,cityrad],
                'Pittsburgh':[40.4417,-80,cityrad],
                'Charlotte':[35.2269,-80.8433,cityrad],
                'Portland':[45.5200,-122.6819,cityrad],
                'San Antonio':[29.4167,-98.5000,0100],
                'Orlando':[28.4158,-81.2989,cityrad],
                'Sacramento':[38.5556,-121.4689,cityrad],
                'Cincinnati':[39.1000,-84.5167,cityrad],
                'Cleveland':[41.4822,-81.6697,cityrad],
                'Kansas City':[39.0997,-94.5786,cityrad]
                }

    closestMetro = [cityrad, '']

    for city in cityDict:
        cityLat = cityDict[city][0]
        cityLong = cityDict[city][1]
        maxDist = cityDict[city][2]
        degrees_to_radians = math.pi/180.0
        phi1 = (90.0 - lat)*degrees_to_radians
        phi2 = (90.0 - cityLat)*degrees_to_radians
        theta1 = long*degrees_to_radians
        theta2 = cityLong*degrees_to_radians
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
        miles = math.acos( cos )*radiusEarth

        if miles < maxDist and miles < closestMetro[1]:
            closestMetro = [miles,city]

    if closestMetro[1] == '':
            closestMetro[1] = 'USA'

    return closestMetro[1] 

lat = 39.0997
lon = -94.5786
a = getCity(lat, lon)
print(a)         
