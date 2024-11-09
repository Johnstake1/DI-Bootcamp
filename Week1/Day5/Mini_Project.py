# MINI PROJECT - TIC TAC TOE

#FOR CHECKER:
# I was not able to create player 2. Therefore it only plays 'X' 

def welcome_message():
    print('WELCOME TO TIC TAC TOE IN PYTHON')

my_list = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']
           ]

def display_board():
    print('***********')    
    for rows in my_list:
            print(" | ".join(rows))
            print('--|---|--')
    print('***********')



player = 'X'
def player_input(player):
    row = int(input('Enter a row\n'))-1
    column = int(input('Enter a column\n'))-1
    while my_list[row][column] != ' ':
        print('This spot is already taken')
        row = int(input('Enter a row\n'))-1
        column = int(input('Enter a column\n'))-1
    my_list[row][column] = player
    display_board()


win_combination = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def check_win(player):
    for combination in win_combination:
        if all(my_list[row][column] == player for row, column in combination):
            print('YOU WIN')
            return True
        else:
             print('THIS GAME IS TIED')

def play():
     player = 'X'
     display_board()

     while True:
          player_input(player)

play()
          
    
          

     
     
     
            

