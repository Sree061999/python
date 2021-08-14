available = ["Monitor", "Mouse", "Keyboard", "CPU", "HDMI cable"]
current_choice = "-"
current_list = [] #empty list
valid_choice = []
for i in range(1, len(available) + 1):
    valid_choice.append(str(i))
while current_choice != '0':
    if current_choice in valid_choice:
        index = int(current_choice) - 1
        chosen_parts = available[index]
        current_list.append(chosen_parts)
        if chosen_parts in current_list:
            print("Removing {} from the list".format(current_choice))
            current_list.remove(chosen_parts)
        else:
            print("Adding {} to the list".format(current_choice))
            current_list.append(chosen_parts)
        print("The list contains: {}".format(current_list))

    else:
        print("Please add options from the list:")
        for number, part in enumerate(available):
            print("{0} : {1}".format(number+1, part))
    current_choice = input()
print(current_list)


