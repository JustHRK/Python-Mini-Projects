# LOGIC
#     R   P   S
# R   0   1  -1
# P  -1   0   1
# S   1  -1   0


# GAME LOGIC
from random import randint
logic_matrix=[[ 0,  1, -1],
              [-1,  0,  1],
              [ 1, -1,  0]] #R P S

def check(comp,player):
    arg=logic_matrix[comp][player]
    match arg:
        case 0:
            print("\nDRAW!")
        case 1:
            print("\nYOU WIN!")
        case -1:
            print("\nYOU LOSE!")

comp=randint(0,2)

# DRIVER

print("---WELCOME TO ROCK, PAPER, and SCISSORS---\n")
print("0-> Rock \n1-> Paper \n2-> Scissors ")
player=int(input(" Your Choice :"))
try:
    if player > 2 or player<0:
        raise ValueError
except ValueError:
    print("Invalid Input")
    exit()

value=["ROCK", "PAPER", "SCISSORS"]
print(f"\nComputer Chose : {value[comp]}\nYou Chose : {value[player]}")
check(comp,player)