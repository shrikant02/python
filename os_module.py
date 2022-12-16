import os

#print(dir(os))

print(os.getcwd()) # current working directory

os.chdir(r'C:\Users\Shubham\Desktop') # change directory

print(os.getcwd())

os.makedirs('OS-Module-Demo\Sub-Dir')

print(os.listdir()) # list directories