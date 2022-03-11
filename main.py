import chess
import replit
from colorama import Fore
from random import randint
board = chess.board()
board.show()

def printhelp():
  print('''https://en.wikipedia.org/wiki/Chess''')
def take_input(msg = ''):
  print(msg)
  print(Fore.YELLOW+' ',end='')
  print(Fore.WHITE,end='')
  return(input())
  
  
def computer_input():
  print('do something cool')
  return



game = True
turn = 'player'

while game:
  if turn == 'player':

    command = str(take_input())
    if command == 'help()':
      print('bro its chess')
      if take_input('Do you really need help? y/n') == 'y':
        printhelp()
    if command == 'quit()':
      rngSUS = randint(0, 9)
      messages = [
      'replit process died due to no pawn structure:',
      'replit process died due to getting forked between its cpu and ram',
      'replit process died due to the player getting their pawn to the end',
      'replit process died due to alex saying it blundered',
      'replit process died due to missing a checkmate in 245',
      'replit process died due to being more sus than a character from among us',
      'replit process died due to death',
      'replit process died due to having 1 core, 1 gb of ram, and 1 gb of storage',
      'replit process died due to not knowing algebraic notation',
      'replit process died due to having a B in PLTW'
      ]
      print(Fore.RED+messages[rngSUS])
      game = False
      
    else:
      if len(command) == 4:
        a = command[0]
        x = str(command[1])
        b = command[2]
        y = str(command[3])
        if a.lower() in "abcdefgh" and x in "12345678":
          if b.lower() in "abcdefgh" and y in "12345678":
            board.move(a+x,b+y)
        replit.clear()
        board.show()
      else:
        print("It should be four digits")