with open("currency.txt","r")as f:
	lines=f.readlines()
	#print(lines)
dic={}
for line in lines:
	data=line.split("\t")
	#print(data)
	dic[data[0]]=data[2]
#print(dic)

amount=int(input("Enter Your Amount: "))
[print(item) for item in dic.keys()]
currency=input("Enter The Contry Name You Have To Convert: ")
print(f"{amount} INR Convert Into {amount * float(dic[currency])} {currency}")


