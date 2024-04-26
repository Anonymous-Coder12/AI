def win(ticTac, x, y):
    if (ticTac[x].count(ticTac[x][y]) == 3):
        return True
    count = 0
    for i in range(3):
        if (ticTac[i][y] == ticTac[x][y]):
            count += 1
    if (count == 3):
        return True
    if (ticTac[0][0] == ticTac[1][1] and ticTac[1][1] == ticTac[2][2] and ticTac[0][0] != "_"):
        return True
    if (ticTac[0][2] == ticTac[1][1] and ticTac[1][1] == ticTac[2][0] and ticTac[1][1] != "_"):
        return True
    return False


def display(ticTac):
    for i in range(3):
        for j in range(3):
            print(ticTac[i][j], end=" ")
        print("\n")


ticTac = [['_' for i in range(3)] for i in range(3)]
arr = []
move = 1
winFlag = False
while (move < 10):
    if (move % 2 == 1):
        n = int(input("player X your move:"))
    else:
        n = int(input("player O your move:"))
    if arr.count(n) == 1:
        print("invalid move")
        continue
    else:
        arr.append(n)
        if move % 2 == 1:
            n -= 1
            x = n//3
            y = n % 3
            ticTac[x][y] = 'X'
            display(ticTac)
            if (win(ticTac, n//3, n % 3) == True):
                print("player X wins")
                break
        else:
            n -= 1
            x = n//3
            y = n % 3
            ticTac[x][y] = 'O'
            display(ticTac)
            if (win(ticTac, n//3, n % 3) == True):
                print("player O wins")
                break
        move += 1
if move > 9:
    print("match draw")
