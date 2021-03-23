
flowerDict = {}
with open("flowers.txt", 'r') as f:
    for line in f:
        flowerDict[line[0]] = line[3:].strip()
def uniqueFlower():
    name = input("Enter your First [space] Last name only: ").title()
    print("Unique flower name that start with the letter {} is {}\n".format(name[0],flowerDict[name[0]]))
uniqueFlower()