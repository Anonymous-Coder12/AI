leftCannibal = 3
leftMiss = 3
rightCannibal = 0
rightMiss = 0
cannibalInBoat = 0
missInBoat = 0
attempts = 0

print("MMMCCC|--->|\n")

while True:
    while True:
        print("Boat going left to right")
        missInBoat = int(input("enter missionary to get in boat:"))
        cannibalInBoat = int(input("enter cannibal to get in boat:"))
        if (missInBoat == 0 and cannibalInBoat == 0) or (missInBoat+cannibalInBoat > 2) or (missInBoat < 0) or (cannibalInBoat < 0) or (leftMiss-missInBoat < 0) or (leftCannibal-cannibalInBoat < 0):
            print("Invalid Choice")
        else:
            break
    leftCannibal -= cannibalInBoat
    leftMiss -= missInBoat
    rightCannibal += cannibalInBoat
    rightMiss += missInBoat
    attempts += 1
    for i in range(leftMiss):
        print("M", end="")
    for i in range(leftCannibal):
        print("C", end="")
    print("|--->|", end="")
    for i in range(rightMiss):
        print("M", end="")
    for i in range(rightCannibal):
        print("C", end="")
    print('\n')
    if (leftCannibal == 0 and leftMiss == 0):
        print("You won the game in", attempts, "attempts")
        break
    if (leftCannibal > leftMiss and leftMiss != 0) or (rightCannibal > rightMiss and rightMiss != 0):
        print("cannibals eat the missionary", "you lose the game", sep="\n")
        break

    while True:
        print("Boat going right to left")
        missInBoat = int(input("enter missionary to get in boat:"))
        cannibalInBoat = int(input("enter cannibal to get in boat:"))
        if (missInBoat == 0 and cannibalInBoat == 0) or (missInBoat+cannibalInBoat > 2) or (missInBoat < 0) or (cannibalInBoat < 0) or (rightMiss-missInBoat < 0) or (rightCannibal-cannibalInBoat < 0):
            print("Invalid choice")
        else:
            break
    leftCannibal += cannibalInBoat
    leftMiss += missInBoat
    rightCannibal -= cannibalInBoat
    rightMiss -= missInBoat
    attempts += 1
    for i in range(leftMiss):
        print("M", end="")
    for i in range(leftCannibal):
        print("C", end="")
    print("|--->|", end="")
    for i in range(rightMiss):
        print("M", end="")
    for i in range(rightCannibal):
        print("C", end="")
    print('\n')
    if (leftCannibal > leftMiss and leftMiss != 0) or (rightCannibal > rightMiss and rightMiss != 0):
        print("cannibals eat the missionary", "you lose the game", sep="\n")
        break
