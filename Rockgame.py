import random

print("===========ROCK PAPER SCISSOR GAME=============")
print("1-ROCK\n2-PAPER\n3.SCISSOR\n4-Exit")
list=['ROCK','PAPER','SCISSOR']

while True:
    a=0
    b=0
    c=' '
    ch=int(input("Enter your choice(1/2/3/4):"))
    if ch not in (1,2,3,4) or c:
        print("invalid")
        continue
    if ch==4:
        break
    print("Your choice:",list[ch-1])
    com=(random.choice(list))
    print("computer choice",com)
    
    if ch==1:
       if list.index(com)==1:
           b+=1
       else:
           a+=1
    if ch==2:
        if list.index(com)==0:
           a+=1
        else:
           b+=1
    if ch==3:
       if list.index(com)==0:
           b=b+1
       else: 
           a+=1
       
    print(f"your score :{a}\ncomputer score: {b}")
    if a>b: print("You are winner")
    elif a<b: print("Computer is winner")
    else: print("draw")
        
