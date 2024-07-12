import os


def get_file_info(**kwargs):
    for v in kwargs.values():
        path = v

    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    if dirname != "":
        dirname = dirname + '/'

    return dirname, filename, file_extension


# print(parse_path(file_path))
print(get_file_info(file_path = 'C:/Users/User/Documents/example.txt'))
print(get_file_info(file_path = 'file_in_current_directory.txt'))
