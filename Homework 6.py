# 1
number1 = 1000, 34007890  # 6 нулів
string = str(number1)
zero_count1 = string.count("0")
print(zero_count1)

# 2
number2 = 1002000
zero_count2 = 0
while number2 % 10 == 0:
    zero_count2 += 1
    number2 //= 10
print(zero_count2)

# 3
my_list_1 = [1, 2, 3, 4]
my_list_2 = [2, 3, 4, 5]
my_result = my_list_1[::2] + my_list_2[::2]
print(my_result)

# 4
my_list4 = [1, 2, 3, 4]
first_value = my_list4.pop(0)
new_list = my_list4
new_list.append(first_value)
print(new_list)

# 5
my_list5 = [1, 2, 3, 4]
first_value = my_list5.pop(0)
my_list5.append(first_value)
print(my_list5)

# 6
txt = "43 > 34 < 56".split(" ")
sum_num = 0
for txt in txt:
    if txt.isdigit():
        sum_num += int(txt)
print(sum_num)

# 7
numbers = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] + numbers[i + 1]:
        count += 1
        print(f"{numbers[i]} > {numbers[i - 1]} + {numbers[i + 1]}")
print(count)

# 8
my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for i in my_list:
    if isinstance(i, str):
        new_list.append(i)
print(new_list)

# 9
my_string = "Hello World!"
my_list1 = []

for i in my_string:
    if my_string.count(i) == 1:
        my_list1.append(i)
print(my_list1)

# 9
my_list = []
value_set1 = {1, 1, 2, 3, 4, 5, "a", "b", "c", "d", "e"}
value_set2 = {1, 3, 5, "b", "d"}

value_set1 = value_set1.intersection(value_set2)
b = len(value_set1)

for i in range(b):
    a = value_set1.pop()
    my_list.append(a)
print(my_list)

# 10
my_string1 = "aaaasdf1"
my_string2 = "asdfff2"

set1 = set(my_string1)
set2 = set(my_string2)

my_list0 = list(set1.intersection(set2))
print(my_list0)

# 11
my_string11 = "aaaasdf1"
my_string22 = "asdfff2"

set11 = set(my_string11)
set22 = set(my_string22)

my_list = list(set11.intersection(set22))
result_list = []

for i in my_list:
    if my_string11.count(i) == 1 and my_string22.count(i) == 1:
        result_list.append(i)
print(result_list)
