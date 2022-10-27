import os
import shutil
from distutils.dir_util import copy_tree
from configuration import path_data, path_old_data, backup, ibdata1
# RUN AS ADMINISTRADOR
shutil.rmtree(path_old_data)

old_name = path_data
new_name = path_old_data
os.rename(old_name, new_name)

# Copy the contents of the backup folder to the data folder
shutil.copy(backup, path_data)

# Copy all the folders of your databases data from mysql/data_old to mysql/data
# Don't copy the folders myql, peroformance_schema, phpmyadmin 
# contents = os.listdir(old_data)
#     for element in contents:
#         isdir = os.path.isdir(element)
#         if(isdir == true and element != 'mysql' and element != 'peroformance_schema' 
#         and element != 'phpmyadmin'):
#             shutil.copy(element, data)

# #  Finally copy the file ibdata1 from data_old to data
# shutil.copy(ibdata1, data)









