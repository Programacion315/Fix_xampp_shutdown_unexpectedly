import os
import shutil
from distutils.dir_util import copy_tree
from configuration import path_data, path_old_data
# Run python as administrator
os.remove(old_data)

old_name = data
new_name = old_data
os.rename(old_name, new_name)

# Create folder 
os.mkdir(data)





