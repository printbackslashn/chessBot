def algebraic(piece):
    # convert e4 into [4, 3]
  column = piece[0].lower()
  row = piece[1]
  row = int(row) - 1 # account for starting at zero
  column = ord(column) - 97 # Use ascii value    
  return [column, row]
  
class board():
  #https://qwerty.dev/chess-symbols-to-copy-and-paste/
  pieces = []
  def show(self):
    # Use chess algebraic coordinate system here
    print("ඞ   A B C D E F G H   ඞ\n")
    for i in range(len(self.pieces)):
        print(i+1, end=" ")
        print("  ", end="")
        for n in self.pieces[i]:
          print(n.name(), end=" ")
        print("  " + str(i+1), end="")
        print("  ")
    print("\nඞ   A B C D E F G H   ඞ")
  def move(self, piece, location):  # Self: self, piece: "e4", location: "e5"

    piece = algebraic(piece) #[column, row]
    location = algebraic(location)
    if self.pieces[piece[1]][piece[0]].canMove(self.pieces, piece, location):
      target = location
      self.pieces[target[1]][target[0]] = self.pieces[piece[1]][piece[0]]
      self.pieces[piece[1]][piece[0]] = blankPiece
    
      
    

  def __init__(self):
    self.pieces = [[blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
    [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece]]
    
    self.pieces[1] = pawn.pawnRow("white")
    self.pieces[0][0] = rook("white")
    self.pieces[0][1] = knight("white")
    self.pieces[0][2] = bishop("white")
    self.pieces[0][3] = queen("white")
    self.pieces[0][4] = king("white")
    self.pieces[0][5] = bishop("white")
    self.pieces[0][6] = knight("white")
    self.pieces[0][7] = rook("white")


    self.pieces[-1][0] = rook("black")
    self.pieces[-1][1] = knight("black")
    self.pieces[-1][2] = bishop("black")
    self.pieces[-1][3] = queen("black")
    self.pieces[-1][4] = king("black")
    self.pieces[-1][5] = bishop("black")
    self.pieces[-1][6] = knight("black")
    self.pieces[-1][7] = rook("black")
    self.pieces[-2] = pawn.pawnRow("black")
class blankPiece():
  canMove = False

  def __init__(self):
    self.canMove = False
  def canMove(self, location):
    return self.canMove
  def name():
      return " "
class king():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    return "K"
class queen():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    return "Q"
class bishop():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    return "B"
class knight():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    return "N"
class rook():
  color = ""
  def __init__(self, color):
    self.color = color
  def name(self):
    return "R"
class pawn():
  color = "white"
  firstMove = False
  def __init__(self, color):
    self.color = color
    self.firstMove = False
  def name(self):
    return "p"
  def pawnRow(color):
    res = []
    for i in range(8):
      res.append(pawn(color))
    return res
  def canMove(self, pieces, piece, location): # self: Self, pieces: Array of pieces, piece: [column, row], location: [column, row]
    if self.color == "white":
      colorChange = 1
    else:
      colorChange = -1
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
    return False
