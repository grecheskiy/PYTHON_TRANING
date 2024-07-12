
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
for i in range(10):

    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()


def rename_files(desired_name, num_digits, source_ext, target_ext):
    counter = 1
    range_name = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(source_ext):
            old_name = os.path.splitext(filename)[0] # get the name without extension
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{desired_name}{str(counter).zfill(num_digits)}.{target_ext}"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            counter += 1


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")



folder_content = ""
files = os.listdir(folder_path)
files.sort()
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)
