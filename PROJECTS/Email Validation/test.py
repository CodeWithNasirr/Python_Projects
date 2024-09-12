email=input('Enter Your Email: ')#skofficial665@gmail.com
k,j,f=0,0,0
if len(email)<6:
    if email[0].isalpha():
        if ("@" in email and email.count("@"==1)):
            if email[-4]=="." or email[-3]==".":
                if "gmail" in email:
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i.isupper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_"or i=="@" or i==".":
                            continue
                        else:
                            f=1
                    if k==1 or j==1 or f==1:
                        print("Wrong 6")
                else:
                    print("Wrong 5")
            else:
                print("Wrong 4")
        else:
            print("Wrong 3")
    else:
        print("Wrong 2")
else:
    print('Wrong 1')