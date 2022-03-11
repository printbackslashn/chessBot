from colorama import Fore

def algebraic(piece):
    # convert e4 into [4, 3]
  column = piece[0].lower()
  row = piece[1]
  row = int(row)  # account for starting at zero 
  column = ord(column) - 97 # Use ascii value  
  print([column, 0-row])
  return [column, 0-row]
  
class board():
  #https://qwerty.dev/chess-symbols-to-copy-and-paste/
  pieces = []
  def show(self):
    
    # Use chess algebraic coordinate system here
    print("♟    A B C D E F G H  ♟")
    print("   ╔═════════════════╗   ")
    for i in range(len(self.pieces)):
        print(8-i, end=" ")
        print(" ║ ", end="")
        for n in self.pieces[i]:
          print(n.name(), end=" ")
          print(Fore.WHITE, end="")
        print("║ " + str(8-i), end="")
        print("  ")
    print("   ╚═════════════════╝   ")
    print("♟    A B C D E F G H  ♟")

  def move(self, piece, location):  # Self: self, piece: "e4", location: "e5"

    piece = algebraic(piece) #[column, row]
    location = algebraic(location)
    if self.pieces[piece[1]][piece[0]].canMove(self.pieces, piece, location):
      target = location
      self.pieces[target[1]][target[0]] = self.pieces[piece[1]][piece[0]]
      self.pieces[piece[1]][piece[0]] = blankPiece
    
      
    

  def __init__(self):
    # How some of the methods work they require a class with the method name, and there is no string.name()
    
    self.pieces = [[blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece]]
    
    self.pieces[1] = pawn.pawnRow("black")
    self.pieces[0][0] = rook("black")
    self.pieces[0][1] = knight("black")
    self.pieces[0][2] = bishop("black")
    self.pieces[0][4] = queen("black")
    self.pieces[0][3] = king("black")
    self.pieces[0][5] = bishop("black")
    self.pieces[0][6] = knight("black")
    self.pieces[0][7] = rook("black")


    self.pieces[-1][0] = rook("white")
    self.pieces[-1][1] = knight("white")
    self.pieces[-1][2] = bishop("white")
    self.pieces[-1][4] = queen("white")
    self.pieces[-1][3] = king("white")
    self.pieces[-1][5] = bishop("white")
    self.pieces[-1][6] = knight("white")
    self.pieces[-1][7] = rook("white")
    self.pieces[-2] = pawn.pawnRow("white")
class blankPiece():
  canMove = False
  color = "blank"
  def __init__(self):
    self.canMove = False
  def canMove(self, x, y): # X y and z because it doesn't need those variables
    return False
  def name():
      return " "
class king():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    if self.color == "white":
      res = Fore.BLUE + "K"
    else:
      res = Fore.RED + "K"
    return res
  def canMove(self, pieces, piece, location): # self: Self, pieces: Array of pieces, piece: [column, row], location: [column, row]
    if pieces[location[0]][location[1]].color == self.color:
      
      return False
    if piece == location:
      return False
    elif piece[0] == location[0]:
      if piece[1] == location[1] + 1:
        return True
      elif piece[1] == location[1] - 1:
        return True
      else:
        return False
    elif piece[1] == location[1]:
      if piece[0] == location[0] + 1:
        return True
      elif piece[0] == location[0] - 1:
        return True
      else:
        return False
    else:
      return False
class queen():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    if self.color == "white":
      res = Fore.BLUE + "Q"
    else:
      res = Fore.RED + "Q"
    return res
class bishop():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    if self.color == "white":
      res = Fore.BLUE + "B"
    else:
      res = Fore.RED + "B"
    return res
class knight():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    if self.color == "white":
      res = Fore.BLUE + "N"
    else:
      res = Fore.RED + "N"
    return res
class rook():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    if self.color == "white":
      res = Fore.BLUE + "R"
    else:
      res = Fore.RED + "R"
    return res
class pawn():
  color = "white"
  firstMove = False
  def __init__(self, color):
    self.color = color
    self.firstMove = False
  def name(self):
    if self.color == "white":
      res = Fore.BLUE + "P"
    else:
      res = Fore.RED + "P"
    return res
  def pawnRow(color):
    res = []
    for i in range(8):
      res.append(pawn(color))
    return res
  def canMove(self, pieces, piece, location): # self: Self, pieces: Array of pieces, piece: [column, row], location: [column, row]
    if self.color == "white":
      colorChange = -1
    else:
      colorChange = 1
    if self.firstMove == False:
      self.firstMove = True
      print("AYO")
      print(f"Piece is {piece} and location is {location}")
      if piece[0] == location[0]: # If going forward
        print('POG')
        if piece[1] == location[1]: # Same place 
          return False
        pieceAhead = piece[1] + colorChange
        if pieceAhead == location[1]: # 1 step forward
          if pieces[pieceAhead][piece[0]].name() == " ":
            return True
        pieceAhead += colorChange
        if pieceAhead == location[1]: # Double step because first move
          if pieces[pieceAhead][piece[0]].name() == " ":
            return True
      elif (piece[0] + 1 == location[0] or piece[0] - 1 == location[0]) and (piece[1] + colorChange == location[1]):
        # Pawn attack
        if pieces[location[0]][location[1]].color != "blank":
          print("Pawn attack")
          return True
    else:
      print("AYyO")
      print(f"Piece is {piece} and location is {location}")
      if piece[0] == location[0]: # If going forward
        print('POG')
        if piece[1] == location[1]: # Same place 
          return False
        pieceAhead = piece[1] + colorChange
        if pieceAhead == location[1]: # 1 step forward
          if pieces[pieceAhead][piece[0]].name() == " ":
            return True 
      elif (piece[0] + 1 == location[0] or piece[0] - 1 == location[0]) and (piece[1] + colorChange == location[1]):
        # Pawn attack
        if pieces[location[0]][location[1]].color != "blank":
          print("Pawn attack")
          return True
    #fine
    return False
