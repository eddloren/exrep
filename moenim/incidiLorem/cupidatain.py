import os

# Create a directory
os.makedirs('my_directory')

# Create a file
with open('my_file.txt', 'w') as f:
    f.write('Hello, world!')
