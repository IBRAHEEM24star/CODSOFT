print("CALCULATOR")
print("1.Addition\n2.Subtraction.\n3.Multuplication.\n4.Division(to find quotient).\n5.modulo(for remainder).")
print("6.Floor division(for quotient without decimal).\n7.Exponentiation.\n8.Exit.")


while True:
    ch=int(input("Enter the choice:"))
    if ch==8:
        break
    num1=int(input("Enter the  first number:"))
    num2=int(input("Enter the second number:"))
    
    if(ch==1):
        print("The addition of {} and {} is {}".format(num1,num2,num1+num2))
    elif(ch==2):
        print("The subtraction of {} and {} is {}".format(num1,num2,num1-num2))
    elif(ch==3):
        print("The multiplication of {} and {} is {}".format(num1,num2,num1*num2))
    elif(ch==4):
        print("The Division of {} and {} is {}".format(num1,num2,num1/num2))
    elif(ch==5):
        print("The modulo of {} and {} is {}".format(num1,num2,num1%num2))
    elif(ch==6):
        print("The Floor division of {} and {} is {}".format(num1,num2,num1//num2))
    elif(ch==7):
        print("The Exponentiation of {} and {} is {}".format(num1,num2,num1**num2))
    else:
        print("Invalid choice.Try again")

