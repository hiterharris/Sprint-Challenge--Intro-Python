import csv

class City:
      
      def __init__(self, name, lat, lon):
            self.name = name
            self.lat = lat
            self.lon = lon
            
      def __str__(self):
            return f"({self.name}, {self.lat}, {self.lon})"
           

cities = []

def cityreader(cities=[]):
    
    with open('cities.csv') as csvfile:
      read = csv.reader(csvfile, delimiter = ',')
      next(read)
      for row in read:
            cities.append(City((row[0]), float(row[3]), float(row[4])))
            
    return cities

cityreader(cities)

for c in cities:
    print(c)
