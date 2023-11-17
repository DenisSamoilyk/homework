import os


# 1, 2
def create_folder_describe(path, reverse=False):
    files = os.listdir(path)

    list_folder = []
    list_files = []
    something_else = []

    for file in files:
        if os.path.isdir(file):
            list_folder.append(file)
        elif os.path.isfile(file):
            list_files.append(file)
        else:
            something_else.append(file)

    some_dict = {
        "folders": sorted(list_folder, reverse=reverse),
        "files": sorted(list_files, reverse=reverse),
        "else": sorted(something_else, reverse=reverse)
    }
    return some_dict


print(create_folder_describe("../Homework", True))


def check_if_correct(all_dicts):
    file_list = []
    new_file_list = []
    folder_list = []

    keys = all_dicts.keys()

    for key in keys:
        one_dict = (all_dicts[key])
        for obj_in_dict in one_dict:
            if "." in obj_in_dict:
                file_list.append(obj_in_dict)
            else:
                folder_list.append(obj_in_dict)

    for item in file_list:
        if os.path.isfile(item):
            new_file_list.append(item)

    for item in file_list:
        if os.path.isdir(item):
            folder_list.append(item)

    return f"{new_file_list}\n{folder_list}"


print(check_if_correct(create_folder_describe("../Homework", True)))
