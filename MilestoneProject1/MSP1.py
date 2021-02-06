def DisplayBoard(board):
    print('\n'*20)
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

def UserInput(board, player, availableIndexes, dictX, dictO):
    inp = 0
    playerMark = PlayerMark(player)
    print(availableIndexes)
    while True:
        inp = int(input(f"Podaj index na który chcesz wstawić {playerMark} (1-9): "))
        if inp in availableIndexes:
            board[inp] = playerMark
            availableIndexes.remove(inp)
            end = CheckWinCondition(player, inp, dictO, dictX)
            break
    return end

def PlayerMark(player):
    if player: return 'X'
    else: return 'O'

def CheckWinCondition(player, inp, dictO, dictX):
    if player:
        for _list in dictX.values():
            if inp in _list:
                _list.remove(inp)
                if len(_list) == 0:
                    print(f"Player: {PlayerMark(player)} won!")
                    return True
    else:
        for _list in dictO.values():
            if inp in _list:
                _list.remove(inp)
                if len(_list) == 0:
                    print(f"Player {player} won!")
                    return True
    return False

def GameLoop():
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = True
    availableIndexes = list(range(1, 10))
    winConditionsDictX = {'1': [1,2,3], '2': [4,5,6], '3': [7,8,9], '4': [1,4,7], '5': [2,5,8], '6': [3,6,9], '7': [1,5,9], '8': [3, 5, 7]}
    winConditionsDictO = {'1': [1,2,3], '2': [4,5,6], '3': [7,8,9], '4': [1,4,7], '5': [2,5,8], '6': [3,6,9], '7': [1,5,9], '8': [3, 5, 7]}
    while True:
        shouldBreak = UserInput(board, player, availableIndexes, winConditionsDictX, winConditionsDictO)
        
        if shouldBreak:
            break
        DisplayBoard(board)
        player = not player

GameLoop()