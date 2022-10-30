import os
import shutil
from distutils.dir_util import copy_tree
from configuration import path_data, path_data_old, backup, ibdata1, location
# RUN AS ADMINISTRADOR
shutil.rmtree(path_data_old)

old_name = path_data
new_name = path_data_old
os.rename(old_name, new_name)

# Copy the contents of the backup folder to the data folder
shutil.copytree(os.path.join(location, "backup"), os.path.join(location, "data"))

# Copy all the folders of your databases data from mysql/data_old to mysql/data
# Don't copy the folders myql, peroformance_schema, phpmyadmin 

# Cannot create a file that already exists !
for element in os.listdir(path_data_old):
    f = os.path.join(path_data_old, element)
    if os.path.isdir(f) == True and element != 'mysql' and element != 'performance_schema' and element != 'phpmyadmin' and element != 'test':
        print(element)
        shutil.copytree(os.path.join(path_data_old, element), os.path.join(path_data, element))
# Finally copy the file ibdata1 from data_old to data
shutil.copy(ibdata1, path_data)
print("Success!!!")









