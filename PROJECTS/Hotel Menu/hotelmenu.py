menu = {
    "Burger": 120,
    "Biryani": 60,
    "ThumsUp": 40,
    "chips": 10
}

print("Welcom to XYZ Hotel")
print("Items Avalible are: ")


[print(item) for item in menu.items()]
sum=0
item_1=input("Enter Your Item What You Want : ")
if item_1 in menu:
    sum+= menu[item_1]
    print(f'Thanks For Ordering {item_1} !')
else:
    print(f"Your Order {item_1} Is Not Avaliable")

another=input("SIr Any Thing Else You Want: YES/NO ")
if another=="YES":
    item_2=input("Enter Your second Item What You Want : ")
    if item_2 in menu:
        sum+= menu[item_2]
        print(f'Thanks For Ordering {item_2} !')

print(f"Your Total Bill is {sum}")




