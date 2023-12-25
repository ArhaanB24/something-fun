import string
import random
import time
alpha = string.ascii_letters
print(alpha)
value = "Virat Kohli" #change value to whatever you want
temp_val = list("1"*len(value))
i = 0
while i!=len(value):
    rand = random.choice(alpha)
    temp_val[i] = rand
    if rand == value[i]:
        i+=1
    elif value[i] == " ":
        temp_val[i] = " "
        i+=1
    print("".join(temp_val[:i+1]))
    time.sleep(0.05)