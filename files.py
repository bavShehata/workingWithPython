f = open("hey.txt", "w")
f.write("hello world!\n")
f.close()


with open("test.txt", "r") as fo :
    data = fo.read()
for line in data:
    print(line, end='')





def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
