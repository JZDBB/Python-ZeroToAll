import os
import shutil
org_path = "./data"
dis_path = './fake'
count = 1
pathes = os.listdir(org_path)
for path in pathes:
    folders = os.listdir(os.path.join(org_path, path))
    for folder in folders:
        path_name = os.path.join(org_path, path, folder)
        filenames = os.listdir(path_name)
        for filename in filenames:
            name = str(count)+ ".jpg"
            shutil.copy(os.path.join(path_name, filename), os.path.join(dis_path, name))
            print(name)
            count += 1