class Library:
    def __init__(self,listofbook):
        self.book=listofbook


    def displaybooks(self):
        for book in self.book:
            print(f'{book}')
        print("Here is The Some List Of Books")
    def borrowbooks(self,bookname):
        if bookname in self.book:
            print(f"Thanks For Pick The {bookname} ! Please Return Withwin 30Days ")
            self.book.remove(bookname)
            return True
        else:
            print(f"This {bookname} book is not avalabile Right Now! ")
            return False
    def ReturnBooks(self,bookname):
        self.book.append(bookname)
        print('Thanks For Returning This Book !')

class Student:
    def borow(self):
        self.book=input("Enter Your Book Name You Want !")
        return self.book
    def Return(self):
        self.book=input("Enter Your Book Name You Want To Return !")
        return self.book

library=Library(["Physics","Chemistry","Math","Hindi"])
student=Student()

if __name__=="__main__":
    while (True):
            wel='''===============Welcome To Library===============
            Enter Your Choice
            1. List of Books
            2. Request a Book
            3. Return/Add a Book
            4. Exits '''
            print(wel)
            try:
                user=int(input("Choice a Number: "))
                if user==1:
                    library.displaybooks()
                elif user==2:
                    library.borrowbooks(student.borow())
                elif user==3:
                    library.ReturnBooks(student.Return())
                elif user == 4:
                    print("Thnks For Visiting our Central Library ")
                    exit()
                else:
                    print("Invalid value")
            except:
                print("Please Enter Valid value")