from distutils import extension
import os
import shutil
from_dir = "C:/Users/Asus/OneDrive/Desktop/Python"
to = "C:/Users/Asus/OneDrive/Desktop/P-111"
list = os.listdir(from_dir)
for file in list:
    name,extension=os.path.splitext(file)
    print(name)