# # 1
# directory_name1 = "Homework 9-test"
# file_name1 = "Utils_domains"
#
# open_file1 = open(f"{directory_name1}/{file_name1}")
# read_file_lines1 = (open_file1.readlines())
#
#
# def get_domains(domains):
#     my_list = []
#
#     for one_domain in domains:
#         remove_dot = one_domain.replace(".", "")
#         my_list.append(remove_dot)
#
#     return my_list
#
#
# print(get_domains(read_file_lines1))
#
# # 2
# directory_name2 = "Homework 9-test"
# file_name2 = "Utils_names"
#
# open_file2 = open(f"{directory_name2}/{file_name2}")
# read_file_lines2 = (open_file2.readlines())
#
#
# def find_name(file_direction):
#     all_letters = []
#     name_list = []
#
#     for one_line in file_direction:
#         for letter_of_line in one_line:
#             if letter_of_line.isspace() or letter_of_line.isalpha():
#                 all_letters.append(letter_of_line)
#
#     turn_into_one_line = "".join(all_letters)
#     split_by_n = turn_into_one_line.split("\n")
#
#     for one_string in split_by_n:
#         t_index = one_string.find("\t")
#         next_t_index = one_string.find("\t", t_index + 1)
#         first_word = one_string[t_index + 1:next_t_index]
#         name_list.append(first_word)
#
#     return name_list
#
#
# print(find_name(read_file_lines2))
