# 1
number1 = 1000, 34007890  # 6 нулів
string1 = str(number1)
zero_count1 = string1.count("0")
print(zero_count1)

# 2
number2 = 1002000
zero_count2 = 0
while number2 % 10 == 0:
    zero_count2 += 1
    number2 //= 10
print(zero_count2)

# 3
my_list3_1 = [1, 2, 3, 4]
my_list3_2 = [2, 3, 4, 5]
my_result3 = my_list3_1[::2] + my_list3_2[::2]
print(my_result3)

# 4
my_list4 = [1, 2, 3, 4]
first_value4 = my_list4.pop(0)
new_list4 = my_list4
new_list4.append(first_value4)
print(new_list4)

# 5
my_list5 = [1, 2, 3, 4]
first_value5 = my_list5.pop(0)
my_list5.append(first_value5)
print(my_list5)

# 6
my_string6 = "43! більше ніж 34, але менше ніж 56."

checkup6_1 = my_string6.replace(",", " ")
checkup6_2 = checkup6_1.replace(".", " ")
checkup6_3 = checkup6_2.replace("!", " ").split()

sum_num6 = 0
for checkup in checkup6_3:
    if checkup.isdigit():
        sum_num6 += int(checkup)
print(sum_num6)

# 7
numbers7 = [2, 4, 1, 5, 3, 9, 0, 7]
count7 = 0

for i in range(1, len(numbers7) - 1):
    if numbers7[i] > numbers7[i - 1] + numbers7[i + 1]:
        count7 += 1
        print(f"{numbers7[i]} > {numbers7[i - 1]} + {numbers7[i + 1]}")
print(count7)

# 8
my_list8 = [1, 2, 3, "11", "22", 33]
new_list8 = []
for i in my_list8:
    if isinstance(i, str):
        new_list8.append(i)
print(new_list8)

# 9.1
my_string9 = "Hello World!"
my_list9 = []

for i in my_string9:
    if my_string9.count(i) == 1:
        my_list9.append(i)
print(my_list9)

# 10.1
my_list01 = []
value_set01_1 = {1, 1, 2, 3, 4, 5, "a", "b", "c", "d", "e"}
value_set01_2 = {1, 3, 5, "b", "d"}

value_set09 = value_set01_1.intersection(value_set01_2)
b = len(value_set01_1)

for i in range(b):
    a = value_set01_1.pop()
    my_list01.append(a)
print(my_list01)

# 10.2
my_string0_1 = "aaaasdf1"
my_string0_2 = "asdfff2"

set0_1 = set(my_string0_1)
set0_2 = set(my_string0_2)

my_list0 = list(set0_1.intersection(set0_2))
print(my_list0)

# 11
my_string01_1 = "aaaasdf1"
my_string02_2 = "asdfff2"

set11 = set(my_string01_1)
set22 = set(my_string02_2)

my_list01 = list(set11.intersection(set22))
result_list01 = []

for i in my_list01:
    if my_string01_1.count(i) == 1 and my_string02_2.count(i) == 1:
        result_list01.append(i)
print(result_list01)
