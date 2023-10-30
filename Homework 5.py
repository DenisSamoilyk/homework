numbers = [20, 50, 90, 100, 150, 200]
for i in numbers:
    if i >= 100:
        print(i)


my_list = []
for i in numbers:
    if i >= 100:
        my_list.append(i)
print(my_list)


my_list = [20, 50]
amount = len(my_list)

if amount < 2:
    my_list.append(my_list[-1] * 10)  # або my_list.append(0)
    print(my_list)
else:
    my_list.append(my_list[-1] + my_list[-2])

print(my_list)
