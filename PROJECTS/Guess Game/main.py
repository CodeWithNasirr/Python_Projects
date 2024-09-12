import random
rand=random.randint(1,100)
print(rand)
user=None
guesses=0
while (user!=rand):
    user=int(input('Enter Your Guess: '))
    guesses+=1
    if user==rand:
        print('You Guess Right')
    else:
        if user<rand:
            print("You Guess it Wrong! Please Enter Large Number")
        else:
            print("You Guess it Wrong! Please Enter Smaller Number")
print(f"You Guess The Number With {guesses} Guesses")

with open("hiscore.txt","r") as f:
    data=int(f.read())
    if guesses<data:
        print("You Just Broke The Hiscore....")
        with open("hiscore.txt","w")as f:
            f.write(str(guesses))
            