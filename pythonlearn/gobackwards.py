data = [104, 150, 23, 179, 300, 250, 110, 161, 50, 100, 140, 168]
min_valid = 100
max_valid = 200
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print("The deleted item is:")
        print("{0} at the position {1}".format(value, top_index - index))
        del data[top_index - index]
print("The final list is \n {}".format(data))
