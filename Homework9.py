# set direction
def set_direction(directory_name="Homework 9-files", file_name="Utils_domains"):
    open_file = open(f"{directory_name}/{file_name}", "r")
    read_file_lines = (open_file.readlines())
    return read_file_lines


# 1
def get_domains(domains):
    my_list = []

    for one_domain in domains:
        remove_dot = one_domain.replace(".", "").replace("\n", "")
        my_list.append(remove_dot)

    return my_list


print(get_domains(set_direction("Homework 9-files", "Utils_domains")))


# 2.1
def find_name1(file_direction):
    all_letters = []
    name_list = []

    for one_line in file_direction:
        for letter_of_line in one_line:
            if letter_of_line.isspace() or letter_of_line.isalpha():
                all_letters.append(letter_of_line)

    turn_into_one_line = "".join(all_letters)
    split_by_n = turn_into_one_line.split("\n")

    for one_string in split_by_n:
        t_index = one_string.find("\t")
        next_t_index = one_string.find("\t", t_index + 1)
        first_word = one_string[t_index + 1:next_t_index]
        name_list.append(first_word)

    return name_list


print(find_name1(set_direction("Homework 9-files", "Utils_names")))


# 2.2
def find_name2(file_direction):
    name_list = []

    for one_line in file_direction:
        split_by_t = one_line.split("\t")
        fnd_name = split_by_t[1]
        name_list.append(fnd_name)

    return name_list


print(find_name2(set_direction("Homework 9-files", "Utils_names")))


# 3
def find_date(text):
    list_month = []  # хотів зробити щось інше але не вийшло потім спробую зробити
    list_date = []
    dict_list = []

    for one_line in text:
        into_str1 = "".join(one_line)
        replace_n = into_str1.replace("\n", "")

        if replace_n.istitle():
            list_month.append(replace_n)  # хотів зробити щоб замість date писалася дата яка в list_month
        else:
            split_by_dash = replace_n.split(" - ")
            list_date.append(split_by_dash[0])

    date = [i for i in list_date if i != ""]

    for i in date:
        into_str2 = "".join(i)
        create_dict = {"date": into_str2}
        dict_list.append(create_dict)

    return dict_list


print(find_date(set_direction("Homework 9-files", "Utils_authors")))

