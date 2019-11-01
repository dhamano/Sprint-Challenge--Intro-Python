import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)
    
    def __str__(self):
        return f"Name: {self.name}, Latitude: {self.lat}, Longitude: {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the 
    # `cities` list
    with open('cities.csv', mode='r') as cities_file:
        cities_data = csv.DictReader(cities_file)
        for row in cities_data:
            cities.append(City(name=row["city"], lat=row["lat"], lon=row["lng"]))
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    maxlat = 0; minlat = 0; maxlon = 0; minlon = 0
    if lat1 > lat2:
        maxlat = lat1
        minlat = lat2
    else:
        maxlat = lat2
        minlat = lat1
    if lon1 > lon2:
        maxlon = lon1
        minlon = lon2
    else:
        maxlon = lon2
        minlon = lon1
    within = [city for city in cities if (minlat <= city.lat <= maxlat) and (minlon <= city.lon <= maxlon)]

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within 
    # the specified coordinates.

    return within

lat1 = 0; lat2 = 0; lon1 = 0; lon2 = 0

def get_coor_1():
    global lat1
    global lon1
    coor1 = input("Enter lat1,lon1:")
    if "," in coor1:
        coor1_arr = coor1.split(", ")
    else:
        coor1_arr = coor1.split(" ")
    if len(coor1_arr) < 2:
        print("please enter: <lattitude> <longitude>")
        get_coor_1()
    else:
        lat1 = float(coor1_arr[0])
        lon1 = float(coor1_arr[1])

def get_coor_2():
    global lat2
    global lon2
    coor2 = input("Enter lat2,lon2:")
    if "," in coor2:
        coor2_arr = coor2.split(", ")
    else:
        coor2_arr = coor2.split(" ")
    if len(coor2_arr) < 2:
        print("please enter: <lattitude> <longitude>")
        get_coor_2()
    else:
        lat2 = float(coor2_arr[0])
        lon2 = float(coor2_arr[1])

def get_coords():
    get_coor_1()
    get_coor_2()

# get_coords()

# city_arr = cityreader_stretch(lat1, lon1, lat2, lon2, cities)

# for city in city_arr:
#     print(city)