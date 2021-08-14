number = input("PLease enter any three numbers:")
in_list = number.split(",")
int_token = []
for i in in_list:
    int_token.append(int(i))
a, b, c = int_token
cal = a + b - c
print(cal)
