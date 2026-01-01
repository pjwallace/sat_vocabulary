import random 
file_path = 'SAT100.txt'

with open(file_path, 'r') as file:
    lines_list = file.readlines()
    print(lines_list)
           

num = random.randint(0,102)
line = lines_list[num].strip()
