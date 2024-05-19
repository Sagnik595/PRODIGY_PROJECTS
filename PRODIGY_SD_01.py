#GUESSING GAME
import random
c=0 #THIS WORKS AS COUNTER
print("==============================================================================================================================")
print("                                                  WELCOME TO THE GUESSING GAME")
print("==============================================================================================================================")
print("ENTER A RANGE WITHIN WHICH YOU WANT THE GENERATED NUMBER:-", end="")
a,b=map(int,input().split(","))
n=random.randint(a,b)
print("There is a number generated between",a,"to",b," \nCan you guess it?")
k=0


while (k!=n):
    k = int(input("TAKE YOUR GUESS:-"))
    c=c+1

    if (k==n):
        break

    else:
        if (k>n):
            print("Too High")
            print("Try again")
        else:
            print("Too Low")
            print("Try again")


print("==============================================================================================================================")
print("!!! YOU WON !!!")
print("THE TOTAL NUMBER OF TRIES YOU TOOK IS:-",c)
print("==============================================================================================================================")