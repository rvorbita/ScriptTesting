theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}



def printBoard(board):
  
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkBoard(board):

    #row
    #for x validation
    if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X' != ' ': 
       print(f"{board['top-L']} wins")
       exit()
    #for o validation
    if board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O' != ' ': 
       print(f"{board['top-L']} wins")
       exit()
    # x
    if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X' != ' ': 
       print(f"{board['mid-L']} wins")
       exit()
    # o
    if board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O' != ' ': 
       print(f"{board['mid-L']} wins")
       exit()
    # x
    if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X' != ' ': 
       print(f"{board['low-L']} wins")
       exit()
    # o  
    if board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O' != ' ': 
       print(f"{board['low-L']} wins")
       exit()

    
    #column
    #X
    if board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X' != ' ':
       print(f"{board['top-L']} wins")
       exit()
    
    if board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X' != ' ':
       print(f"{board['top-M']} wins")
       exit()


    if board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X' != ' ':
       print(f"{board['top-R']} wins")
       exit()  
    
    #O
    if board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O' != ' ':
       print(f"{board['top-L']} wins")
       exit()    

    if board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O' != ' ':
       print(f"{board['top-M']} wins")
       exit()

    if board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O' != ' ':
       print(f"{board['top-R']} wins")
       exit()



    # diagonal \
    if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X' != ' ':
        print(f"{board['top-L']} wins")
        exit()

    if board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O' != ' ':
       print(f"{board['top-L']} wins")
       exit()


    # diagonal /
    if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X' != ' ':
        print(f"{board['top-L']} wins")
        exit()

    if board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O' != ' ':
       print(f"{board['top-L']} wins")
       exit()




turn = 'X'
for i in range(9):
  printBoard(theBoard)
  checkBoard(theBoard)
  print('Turn for ' + turn + '. Move on which space?')
  move = input()
  theBoard[move] = turn
  if turn == 'X':
    turn = 'O'
  else:
    turn = 'X'



printBoard(theBoard)
