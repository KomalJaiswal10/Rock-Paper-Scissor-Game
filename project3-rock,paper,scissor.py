import random

name = input("Enter your name :")
print()


d={1:'rock',2:'paper',3:'scissor'}


i=1


us=0
ss=0

while True:
    
    
    print("Round No.",i)
    print("enter your choice")
    uip=int(input("(1: rock , 2: paper , 3: scissor , 4: Exit)= "))
    sip=random.randint(1,3)
    print()

    if uip in d:
        pass

    elif uip==4:
        print("Okay...!!")
        break
    
    else:
        print("invalid input")
        print("-------------------------------------")
        continue

   

    if uip==1 and sip==2:
        print(name.capitalize(),"Wins")
        us+=1
        print()
        print("Total Score")
        print(name.capitalize() ,":", us, "System :",ss)
    
    elif uip==2 and sip==1:
        print("System Wins")
        ss+=1
        print()
        print("Total Score")
        print(name.capitalize() ,":", us,",", "System :",ss)

        
    elif uip==1 and sip==3:
        print(name.capitalize(),"Wins")
        us+=1
        print()
        print("Total Score")
        print(name.capitalize() ,":", us,",", "System :",ss)

        
    elif uip==3 and sip==1:
        print("System Wins")
        ss+=1
        print()
        print("Total Score")
        print(name.capitalize() ,":", us, ",","System :",ss)
        
    elif uip==3 and sip==2:
        print(name.capitalize(),"Wins")
        us+=1
        print()
        print("Total Score")
        print(name.capitalize() ,":", us,",", "System :",ss)
        
    elif uip==2 and sip==3:
        print("System Wins")
        ss+=1
        print()
        print("Total Score")
        print(name.capitalize() ,":", us,",", "System :",ss)

    
        
    
    elif uip==sip:
        print("Tie")
        print("------------------------------------------------")
        us=us
        ss=ss
        continue
    
    
    print("------------------------------------------------")
    i+=1

    
print("------------------------------------------------")
print("Total Score")
print(name.capitalize() ,":", us,",", "System :",ss)




























    

