print("Press x for stop Calculator")
sum=0
while(True):
    user=(input('Enter a Number: '))
    if user=="x":
        break
    sum=sum + int(user)
    print(f"Order Total so Far {sum}")

print(f"The Total Price is {sum}")