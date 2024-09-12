import string
import random

f1=string.ascii_lowercase
f2=string.ascii_uppercase
f3=string.digits
f4=string.punctuation

user=int(input("Enter pass Lenght "))

f=[]
f.extend(f1)
f.extend(f2)
f.extend(f3)
f.extend(f4)

print("".join(random.sample(f,user)))