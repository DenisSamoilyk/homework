class FileProcessor:
    def __init__(self, directory_name="Homework 9-files"):
        self.directory_name = directory_name

    def set_direction(self, file_name):
        file_path = f"{self.directory_name}/{file_name}"
        with open(file_path, "r") as open_file:
            read_file_lines = open_file.readlines()
        return read_file_lines

    @staticmethod
    def get_domains(domains):
        my_list = []
        for one_domain in domains:
            remove_dot = one_domain.replace(".", "").replace("\n", "")
            my_list.append(remove_dot)
        return my_list

    @staticmethod
    def find_name(file_direction):
        name_list = []
        for one_line in file_direction:
            split_by_t = one_line.split("\t")
            fnd_name = split_by_t[1]
            name_list.append(fnd_name)
        return name_list

    @staticmethod
    def find_date(text):
        list_month = []
        list_date = []
        dict_list = []

        for one_line in text:
            into_str1 = "".join(one_line)
            replace_n = into_str1.replace("\n", "")

            if replace_n.istitle():
                list_month.append(replace_n)
            else:
                split_by_dash = replace_n.split(" - ")
                list_date.append(split_by_dash[0])

        date = [i for i in list_date if i != ""]

        for i in date:
            into_str2 = "".join(i)
            create_dict = {"date": into_str2}
            dict_list.append(create_dict)

        return dict_list


file_processor = FileProcessor()
domains_result = file_processor.get_domains(file_processor.set_direction("Utils_domains"))
print(domains_result)

names_result = file_processor.find_name(file_processor.set_direction("Utils_names"))
print(names_result)

date_result = file_processor.find_date(file_processor.set_direction("Utils_authors"))
print(date_result)
