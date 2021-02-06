def DisplayBoard(board):
    print('\n'*20)
    print("#############")
    print("#   #   #   #")
    print(f"# {board[1]} # {board[2]} # {board[3]} #")
    print("#   #   #   #")
    print("#############")
    print("#   #   #   #")
    print(f"# {board[4]} # {board[5]} # {board[6]} #")
    print("#   #   #   #")
    print("#############")
    print("#   #   #   #")
    print(f"# {board[7]} # {board[8]} # {board[9]} #")
    print("#   #   #   #")
    print("#############")

def UserInput(board, playerMark, availableIndexes):
    inp = 0
    while True:
        inp = int(input(f"Podaj index na który chcesz wstawić {playerMark} (1-9): "))
        if inp in availableIndexes:
            board[inp] = playerMark
            availableIndexes.remove(inp)
            break
    return inp

def PlayerMark(player):
    if player: return 'X'
    else: return 'O'

def CheckWinCondition(index, dictionary):
    for _list in dictionary.values():
        if index in _list:
            _list.remove(index)
            if len(_list) == 0: return True
    return False

def ShouldBreak(playerMark, index, dictO, dictX):
    if playerMark == 'X': return CheckWinCondition(index, dictX)
    else: return CheckWinCondition(index, dictO)

def GameLoop():
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = True
    availableIndexes = list(range(1, 10))
    winConditionsDictX = {'1': [1,2,3], '2': [4,5,6], '3': [7,8,9], '4': [1,4,7], '5': [2,5,8], '6': [3,6,9], '7': [1,5,9], '8': [3, 5, 7]}
    winConditionsDictO = {'1': [1,2,3], '2': [4,5,6], '3': [7,8,9], '4': [1,4,7], '5': [2,5,8], '6': [3,6,9], '7': [1,5,9], '8': [3, 5, 7]}
    DisplayBoard(board)

    while True:
        playerMark = PlayerMark(player)
        index = UserInput(board, playerMark, availableIndexes)
        DisplayBoard(board)
        if ShouldBreak(playerMark, index, winConditionsDictO, winConditionsDictX):
            print(f"Gracz {playerMark} wygrał")
            break
        if len(availableIndexes) == 0:
            print("Nikt nie wygrał")
            break
        player = not player

GameLoop()