# read input file and save contents
file = open('day4.txt', 'r')
lines = file.readlines()

# get drawed numbers, init "board" to store all boards
drawed_numbers = [int(i) for i in lines[0].split(",")]
boards = []

# make boards from input (ugly implementation but it works)
for i in range(len(lines[1:])):
    if lines[i] == "\n":
        board = []
        board.append(list(map(int, lines[i+1].rstrip("\n").split())))
        board.append(list(map(int, lines[i+2].rstrip("\n").split())))
        board.append(list(map(int, lines[i+3].rstrip("\n").split())))
        board.append(list(map(int, lines[i+4].rstrip("\n").split())))
        board.append(list(map(int, lines[i+5].rstrip("\n").split())))
        boards.append(board)


# --------------------------- Part 1 ---------------------------

# solves the puzzle 
def play(boards, list_of_nums):

    for num in list_of_nums:
        for board in boards:
            mark_board(board, num)
            if winner(board):
                return get_score(board, num)
            else:
                continue
    
    # if none of the conditions pass, return False (error)
    return False

# takes a board and determines if its a winner
def winner(board):
    # check for horizontal winner
    for i in range(5):
        if (board[i][0] == "X" and board[i][1] == "X" and 
            board[i][2] == "X" and board[i][3] == "X" and 
            board[i][4] == "X"):
            return True
    
    # check for vertical winner
    for i in range(5):
        if (board[0][i] == "X" and  board[1][i] == "X" and 
            board[2][i] == "X" and  board[3][i] == "X" and 
            board[4][i] == "X"):
            return True

    # no winner, so return false
    return False

# takes a board and a number, and marks the board if the number is present
def mark_board(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = "X"
    
    return board

# gets the score of the board
def get_score(board, number):
    sum = 0
    for row in board:
        for num in row:
            if num == "X":
                continue
            else: 
                sum += num
    
    return sum * number

# get the answer!
# print(play(boards, drawed_numbers))


# --------------------------- Part 2 ---------------------------


# solves the puzzle
def play_for_squid(boards, list_of_nums):
    
    while True:
        for num in list_of_nums:
            for board in boards:
                mark_board(board, num)
            for board in boards:
                if winner(board):
                    if len(boards) == 1:
                        print("got here")
                        print("whats the score?")
                        return get_score(board, num)
                    else:
                        boards.remove(board)

# gets the answer!
# print(play_for_squid(boards, drawed_numbers))