import string
import random

f1=string.ascii_lowercase
f2=string.ascii_uppercase
f3=string.digits
f4=string.punctuation


x=[]

x.extend(f1)
x.extend(f2)
x.extend(f3)
x.extend(f4)

user=int(input('Enter a Number: '))

print(''.join(random.sample(x,user)))