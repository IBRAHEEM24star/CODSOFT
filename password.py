import random
import string
def password_generator(length,level):
    if level==1:
        key=string.ascii_letters
    elif level==2:
        key=string.ascii_letters + string.digits
    elif level==3:
        key=string.ascii_letters+string.digits+string.punctuation
    else:
        print("Invalid choice so strong password will be generated")
        key=string.ascii_letters+string.digits+string.punctuation

    password ="".join(random.choice(key) for _ in range(lenght))
    return password
try:
   lenght=int(input("Enter the lenght of password :"))
   if lenght<4 :
      print("Password lenght should be greater than 4")
   else:
      print("Choose the complexity level:")
      print("1.low.\n2.medium\n3.high")
      level=int(input("Enter the choice(1/2/3):"))

      password=password_generator(lenght,level)

      print("Generated Password:",password)
except ValueError:
    print("Invalid choice,try again.")
    
