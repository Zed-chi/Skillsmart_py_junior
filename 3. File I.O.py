"""
Python File R/W

"""

# Запись файлов
import random
for i in range(1,11):
    name = str(i)+".txt"
    f = open(name,"a")
    for j in range(3):
        f.write(str(random.randint(0,1000))+"\n")
    f.close()
 
    
# Чтение
import sys

a = sys.argv[1]
b = sys.argv[2]

name1 = str(a)+".txt"
name2 = str(b)+".txt"

def get_num(name):
    total = 0
    with open(name, "r") as f:
        for i in range(3):
            total+= int(f.readline())
    return total

print(get_num(name1)+get_num(name2))