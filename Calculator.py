x=1
while x>=1:
    print("Welcome to calculator")
    print("For addition type add")
    print("For subtraction type subtract")
    print("For multiplication type multiply")
    print("For division type divide")
    user_input = input(" :")
    num1= float(input("Enter a number:"))
    num2= float(input("Enter another number:"))
    if user_input == "add":
        print(num1,"+",num2,"=",num1+num2)
    elif user_input == "subtract":
        print(num1,"-",num2,"=",num1-num2)
    elif user_input == "multiply":
        print(num1,"*",num2,"=",num1*num2)
    elif user_input == "divide":
        print(num1,"/",num2,"=",num1/num2)
    else:
        print("Incorrect input")
    x=x+1
