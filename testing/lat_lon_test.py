
from geopy.distance import distance, Point


# input coordinates
lat1 = 40.10891
lon1 = -83.09286
lat2 = 41.87811
lon2 = -87.62980

# create point objects from input coordinates
point1 = Point(lat1, lon1)
point2 = Point(lat2, lon2)

# calculate the distance between the two points in meters
dist = distance(point1, point2).km

print(dist)

