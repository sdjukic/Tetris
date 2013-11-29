# Beginning of my implementation of RL for Tetris

# This is where I will define tetromino pieces
# They will be stored as 5x5 matrix 
# Like board, their occupied spaces will be marked by one's
# and free spaces by zero's
# Each tetromino can have different rotations 

# After all this is not a class. I looked up the solution that dude
# that wrote GUI version is using and I liked it
# Each shape is list of lists (possible ways to orient tetromino).
# And finally all of them are brought toghether in the dictionary

sShape = [['00000','00000','00110','01100','00000'],
          ['00000','00100','00110','00010','00000']]
zShape = [['00000','00000','01100','00110','00000'],
          ['00000','00100','01100','01000','00000']]
iShape = [['00100','00100','00100','00100','00000'],
          ['00000','00000','11110','00000','00000']]
oShape = [['00000','00000','01100','01100','00000']]
jShape = [['00000','01000','01110','00000','00000'],
          ['00000','00110','00100','00100','00000'],
          ['00000','00000','01110','00010','00000'],
          ['00000','00100','00100','01100','00000']]
lShape = [['00000','00010','01110','00000','00000'],
          ['00000','00100','00100','00110','00000'],
          ['00000','00000','01110','01000','00000'],
          ['00000','01100','00100','00100','00000']]
tShape = [['00000','00100','01110','00000','00000'],
          ['00000','00100','00110','00100','00000'],
          ['00000','00000','01110','00100','00000'],
          ['00000','00100','01100','00100','00000']]

Pieces = {'s':sShape, 'z':zShape, 'j': jShape, 'l':lShape, 'i':iShape, 'o':oShape, 't':tShape}



# let's create a board that will know it's state 
# and where will piece land

class Board:
  "Board for Tetris. It will be 20x10 in size, know its state and will know where will next piece land aka get stuck"
  # board will be represented as matrix aka table
  # zero's will be free spaces and one's occupied
  def __init__(self, x = 20, y = 10):
    self.noRows = x
    self.noCols = y
    # create a single row
    row = ['0'*10]
    # multiply it row number of times to create a table
    self.table = [row for x in xrange(x)]
    # this vector will store the height of the top piece for the column
    # will be used to resolve collisions
    self.pieceVector = [0] * 10

  # debugging function that will display my current status of the table
  def display(self):
    for x in range(self.noRows):
      print self.table[x],
      print

  # this function will just return pieceVector
  def getPieceVector(self):
    return self.pieceVector

  # function will place piece on the board
  # assume that it will fall straight down from this position
  # no one will move it during the fall (agent will do this in less than a second anyway
  # we need type of the piece, its orientation (rotation) and y position 
  # pieces are placed in 5x5 matrices
  # so this is function that should resolve colisions. Once tetromino collide with something on
  # the board it should stop.
  # This yCoo is the top left coordinate of the matrix that defines tetromino. Note that it can
  # be negative, as long as leftmost one of the tetromino is inside board.
  #def placePiece(tetromino, yCoo):



  # helper function that will return the leftmost and rightmost position that we can put
  # tetromino on the board
  # It returns pair of values:
  # both correspond to the leftmost position of top left corner of tetromino matrix
  # first is it's leftmost position and second is its righmost position
  # so agent can place tetromino anywhere in that range
  def calculateExtremes(self, aTetromino):
    leftExtreme = 5
    rightExtreme = 0
    for row in aTetromino:
      counter = 0
      for element in row:
        if element == '1':
          if counter < leftExtreme:
            leftExtreme = counter
          if counter > rightExtreme:
            rightExtreme = counter
        counter += 1

    return (-leftExtreme, 9 - rightExtreme) 

  # NOTE: I really don't see a reason for this to be a member of Board class
  # except that conceptually it is functionality that comes outside of agent
  # so it is provided by the board.
  # this function will call calculateExtremes to calculate leftmost and rightmost
  # positions and pack them together with the rotation that tetromino can take
  # so agent can choose where it wants to place it
  def tetrominoLimit(self, tetromino):
    noRotations = len(tetromino)
    # this will be list of triples
    # first value will be tetromino rotation
    # second the leftmost position it can take (upper left corner of its matrix)
    # third is the rightmost positin it can take
    tPositions = []
    for rotation  in range(noRotations):
      leftmost, rightmost = self.calculateExtremes(tetromino[rotation])
      tPositions.append((rotation, leftmost, rightmost))

    return tPositions   

  # function that will scan the board to update it's state and PieceVector
  # function accepts the tetromino we are placing on the board with 
  # x and y coordinate of its top-left corner
  # collisionHeight is the value given by detectCollision function
  # the coordinate where tetromino collided with something on the board
  def scanBoard(self, tetromino, xCoo, yCoo, collisionHeight):
    for x in range(self.noRows):
      for y in range(self.noCols):
        if collisionHeight <= x < xCoo:
          if yCoo - 5 <= y < yCoo:
            if tetromino[


  # this function should detect the collision between tetromino and 
  # other pieces that are on the board
  # once the tetromino collided it should be added to the PieceVector
  # aka PieceVector should be updated
  def detectCollision(aTetromino, yPosition):
     

  
# let's see how this works
myBoard = Board()
print "I have created a board"
#print "Now let's display it"
#myBoard.display()
print "How does the piece vector look like "
print myBoard.getPieceVector()

# to randomly create tetromino we have to import randint
from random import choice

# now let's create a function that will return a tetromino when we ask it
def getTetromino():
  return Pieces[choice(Pieces.keys())]

# how does this work
tetromino = getTetromino()
print "Our tetromino has %i ways to rotate." %(len(tetromino))
for i in range(len(tetromino)):
  for row in tetromino[i]:
    print row
# let's get possible rotations of tetromino and range in columns where
# we can put it
possibilities = myBoard.tetrominoLimit(tetromino)
for pos in possibilities:
  print "We can place tetromino between %i - %i " %(pos[1], pos[2])

