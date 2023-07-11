#make a simple calculator that can add, subtract, multiply and divide using functions
def confirm():
    user_input=input("Do you want to perform a calculation (y/n)")
    if user_input=="y" or "Y":
        print(
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
        )
    else:
        exit()


def add():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1+num2)
def subtract():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1-num2)
def multiply():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1*num2)
def divide():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1/num2)
confirm()
user_choice=int(input("Enter your choice: "))
if user_choice==1:
    add()
elif user_choice==2:
    subtract()
elif user_choice==3:
    multiply()
elif user_choice==4:
    divide()




