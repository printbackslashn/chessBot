import chess

from colorama import Fore
from random import randint

board = chess.board()
board.show()

messages = [
      'process died due to no pawn structure:',
      'process died due to getting forked between its cpu and ram',
      'process died due to the player getting their pawn to the end',
      'process died due to alex saying it blundered',
      'process died due to missing a checkmate in 245',
      'process died due to being more sus than a character from among us',
      'process died due to death',
      'process died due to having 1 core, 1 gb of ram, and 1 gb of storage',
      'process died due to not knowing algebraic notation',
      'process died due to having a B in PLTW'
      ]

def printhelp():
  print('''https://en.wikipedia.org/wiki/Chess''')
def take_input(msg = ''):
  print(msg)
  print(Fore.LIGHTYELLOW_EX+' ',end='')
  print(Fore.WHITE,end='')
  return(input())
  
  
def computer_input():
  print('do something cool')
  return

def reload():
  print('\033c')
  board.show()

def player_input():
  global game
  global turn
  command = str(take_input())
  #default commands
  if command == 'quit()':
    rngSUS = randint(0, 9)
    print(Fore.RED+messages[rngSUS])
    game = False

  if command == 'reload':
    reload()
    
  #making moves  
  else:
    while len(command) != 4:
      print('This needs to be 4 digits')
      command = str(take_input())
    a = command[0]
    x = str(command[1])
    b = command[2]
    y = str(command[3])
    if a.lower() in "abcdefgh" and x in "12345678":
      if b.lower() in "abcdefgh" and y in "12345678":
        moveRes = board.move(a+x,b+y)
        print(moveRes)
        if not(moveRes):
          turn -= 1
        turn+=1
        if turn == 2:
          turn=0
          #binary toggle
        reload()


game = True
turn = 0

while game:
  if turn == 0:#White
    print('Its Whites turn.')
    player_input()
  if turn == 1: #Black
    print('Its Blacks turn.')
    player_input()
