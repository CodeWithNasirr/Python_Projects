import random

def Game(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True


print("Comp Turn: :Snake(s),Water(w),Gun(g)")
rand=random.randint(1,3)

if rand==1:
    comp="s"
elif rand==2:
    comp="w"
elif rand==3:
    comp="g"

you=input("Your Turn: :Snake(s),Water(w),Gun(g)")

print(f"Comp Choose : {comp}")
print(f"You Choose : {you}")
f=Game(comp,you)

if f==None:
    print("The Game is Tie!")
elif f==True:
    print("You Won!")
else:
    print("You Lose!")