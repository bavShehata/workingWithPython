def show(x= True,y=29):
    print (x,y)


show(4,y = 5)



egg_count = 0

def buy_eggs():
    egg_count = 12 # purchase a dozen eggs

buy_eggs()


numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]


averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)



cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]


short_cities = list(filter(lambda city: len(city) < 10, cities))
print(short_cities)