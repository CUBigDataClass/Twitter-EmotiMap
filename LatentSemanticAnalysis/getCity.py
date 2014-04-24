#!/usr/bin/python
import math

def getCity(lat,long):

    radiusEarth = 3960

    cityDict = {'New York': [40.67,73.94,100],
                'Los Angeles': [34.05, 118.25,100],
                'Chicago': [41.8819, 87.6278,100],
                'Dallas': [32.7758, 96.7967,100],
                'Houston': [29.7628, 95.3831, 100],
                'Philadelphia': [39.95,75.17,100],
                'Washington': [38.8951, 77.0368,100],
                'Maimi': [25.7877, 80.2241,100],
                'Atlanta':[33.7550, 84.3900,100],
                'Boston':[42.3581,71.0636,100],
                'San Francisco':[37.7833,122.4167,100],
                'Phoenix': [33.4500,112.0667,100],
                'Riverside': [33.9481, 117.3961,100],
                'Detroit': [42.3314, 83.0458,100],
                'Seattle': [47.6097, 122.3331, 100],
                'Minneapolis':[44.9833, 93.2667,100],
                'San Diego': [32.7150, 117.1625,100],
                'Tampa': [27.9710, 82.4650,100],
                'St. Louis': [38.6272, 90.1978, 100],
                'Baltimore': [39.2833, 76.6167,100],
                'Denver': [39.7392, 104.9847,100],
                'Pittsburgh':[40.4417,80,100],
                'Charlotte':[35.2269,80.8433,100],
                'Portland':[45.5200,122.6819,100],
                'San Antonio':[29.4167,98.5000,100],
                'Orlando':[28.4158,81.2989,100],
                'Sacramento':[38.5556,121.4689,100],
                'Cincinnati':[39.1000,84.5167,100],
                'Cleveland':[41.4822,81.6697,100],
                'Kansas City':[39.0997,94.5786,100]
                }

    closestMetro = [100000, '']

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
            closestMetro[1] = 'Other'

    return closestMetro[1] 
            
