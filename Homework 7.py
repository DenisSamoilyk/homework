# 1
my_list1 = ["qwe", "abc", 1234, "Hello"]
new_list1 = []

for count, list_word in enumerate(my_list1):
    if count % 2:
        new_list1.append(list_word)
    else:
        conversion = str(list_word)
        flip = conversion[::-1]
        new_list1.append(flip)

print(new_list1)

# 2
my_list2 = ["ABC", "cuba", "abc", "def"]
new_list2 = []

for i in my_list2:
    lower_case = i.lower()
    first_letter = lower_case[0]
    if first_letter == "a":
        new_list2.append(i)

print(new_list2)

# 3
my_list3 = ["ABC", "cuba", "abc", "def"]
new_list3 = []

for i in my_list3:
    lower_case = i.lower()
    find_letter = lower_case.find("a")
    find_a = lower_case[find_letter]
    if find_a == "a":
        new_list3.append(i)

print(new_list3)

# 4.a
count = 0
users = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Jonathan", "age": 17}]
name = []
age = []

for user in users:
    find_age = users[count]["age"]
    age.append(find_age)
    count += 1
min_age = min(age)
for user in users:
    if user["age"] == min_age:
        name.append(user["name"])

print(name)

# 4.б
count = 0
users = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Jonathan", "age": 17}]
size_name = []
name_len = []

for user in users:
    find_name = users[count]["name"]
    a = len(find_name)
    name_len.append(a)
    count += 1

max_len = max(name_len)
for user in users:
    if len(user["name"]) == max_len:
        size_name.append(user["name"])

print(size_name)

# 4.в
count = 0
users = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Jonathan", "age": 17}]
age = []

for user in users:
    find_age = users[count]["age"]
    age.append(find_age)
    count += 1

number_of_users = len(age)
age_users = sum(age)
print(age_users // number_of_users)

# 5
my_dict_1 = {1: 1,
             2: 2,
             3: 3,
             5: 25,
             11: 100
             }

my_dict_2 = {
             2: 22,
             4: 400,
             10: 15,
             11: 11,
             }

my_list = []

# 5.а
find_same = list(set(my_dict_1).intersection(set(my_dict_2)))
print(find_same)

# 5.б
find_difference = list(set(my_dict_1).difference(set(my_dict_2)))
print(find_difference)

# 5.в
find_difference_keys = list(set(my_dict_1).difference(set(my_dict_2)))

for key in find_difference_keys:
    key_obj = my_dict_1[key]
    key_value = key, key_obj
    my_list.append(key_value)

print(dict(my_list))

# 5.г
find_difference_keys_1 = list(set(my_dict_1).difference(set(my_dict_2)))
find_difference_keys_2 = list(set(my_dict_2).difference(set(my_dict_1)))

for key in find_difference_keys_1:
    key_obj = my_dict_1[key]
    key_value = key, key_obj
    my_list.append(key_value)

for key in find_difference_keys_2:
    key_obj = my_dict_2[key]
    key_value = key, key_obj
    my_list.append(key_value)

find_same_keys = list(set(my_dict_1).intersection(set(my_dict_2)))

for key in find_same_keys:
    key_obj1 = my_dict_1[key]
    key_obj2 = my_dict_2[key]
    key_value = key, [key_obj1, key_obj2]
    my_list.append(key_value)

print(dict(my_list))
