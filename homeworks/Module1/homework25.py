import os
directory = 'D:\\Steam\\steamapps\\workshop\\content\\784150'
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(directory))
    for file in filenames:
        full_name_path = dirpath + '\\' + file
        print(os.path.getmtime(full_name_path))
        print(os.path.getsize(full_name_path))
        print(os.path.join(full_name_path))