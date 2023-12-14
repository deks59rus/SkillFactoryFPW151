board = ['1',  '2', '3','4',  '5', '6', '7',  '8', '9']
game_continue = True
round_count =1
VictoryLines=\
[
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ['1','4','7'],
    ['2','5','8'],
    ['3','6','9'],
    ['3','5','7'],
    ['1','5','9']
]

def Round():
    global round_count
    print(f"Раунд {round_count}!")
    Print(board)
    turn = UserInput()
    MakeTurn(turn[0], turn[1])
    round_count +=1
    WinCheck()

def WinCheck():
    global game_continue
    for x in VictoryLines:
        if  x[0]==x[1] and x[0]== x[2] and str(x[0]) == "x":
            print("Крестики победили!")
            game_continue = False
            break
        elif x[0]==x[1] and x[0]== x[2] and str(x[0]) == "o":
            print("Нолики победили!")
            game_continue =False
            break
    if  game_continue:
        Round()

def MakeTurn(sqare, char):
    global board, VictoryLines, round_count
    changed = False
    for a in board:
        if a == sqare:
            board[board.index(a)] = char
            changed =True
    if not changed:
        print("Эта клетка уже занята! Выберите другую")
        round_count-=1
        return
    for line in VictoryLines:
        for sym in line:
            if sym == sqare:
               VictoryLines[VictoryLines.index(line)][line.index(sym)]= char

def UserInput():
    player = 2-round_count%2
    exeption = False
    print (f"Ход игрока {player}")
    if player == 1:
        print (f"Игрок {player} (X) - крестики, пожалуйста введите номер клетки от 1 до 9 (формата 1о, 4х) клетку и симбвол(\'o\'/\'x\')")
    else:
        print (f"Игрок {player} (О) -нолики, пожалуйста введите номер клетки от 1 до 9 (формата 1о, 4х) клетку и симбвол(\'o\'/\'x\')")

    result = str(input()).lower()
    while len(result) !=2:
        print("Некорректная длина ввода!\n")
        exeption=True
        break
    while int(result[0]) > 9 or int(result[0]) <=0:
        print("Пожалуйста введите корректный порядковый номер незанятой клетки!\n")
        exeption=True
        break
    while result[1] != 'o' and result[1] != 'x':
        print("Пожалуйста введите корректный латинский симбвол(\'o\'/\'x\')\n")
        exeption=True
        break
    while (result[1] == 'o'and player ==1) or (result[1] == 'x' and player ==2):
        print("Пожалуйста, учитывайте порядок хода! Сейчас ход другого игрока!\n")
        exeption=True
        break
    if  exeption==False:
        return result
    else:
        result=UserInput()
        return result

def Print(board):
    i=0
    for x in board:
        print(x, end=' ')
        i=i+1
        if i == 3:
            print()
            i=0

while game_continue:
    Round()
