import sys

instructions = "Input position you would like to play in the format \"R C\" where R is the row and C is the column."

class Match:
	def __init__(self):
		self.board = [[ ' ' , ' ' , ' '],
            		  [ ' ' , ' ' , ' '],
             		  [ ' ' , ' ' , ' ']]

		self.turn = "Player X"
		self.status = "Ongoing"

	def __repr__(self):
		return "repr"

	def __str__(self):
		return "\nMake your move: %s\n%s\n%s\n%s" % (self.turn,repr(self.board[0]),repr(self.board[1]),repr(self.board[2]))

	def checkForW(symbol):
		if self.board[0][0] == symbol and
		   self.board[0][1] == symbol and
           self.board[0][2] == symbol: self.status = "Player %s wins!" % upper(symbol)
	    if self.board[1][0] == symbol and
		   self.board[1][1] == symbol and
           self.board[1][2] == symbol: self.status = "Player %s wins!" % upper(symbol)
		if self.board[2][0] == symbol and
		   self.board[2][1] == symbol and
           self.board[2][2] == symbol: self.status = "Player %s wins!" % upper(symbol)
		if self.board[0][0] == symbol and
		   self.board[1][0] == symbol and
           self.board[2][0] == symbol: self.status = "Player %s wins!" % upper(symbol)
		if self.board[0][1] == symbol and
		   self.board[1][1] == symbol and
           self.board[2][1] == symbol: self.status = "Player %s wins!" % upper(symbol)
		if self.board[0][2] == symbol and
		   self.board[1][2] == symbol and
           self.board[2][2] == symbol: self.status = "Player %s wins!" % upper(symbol)

		if self.board[0][0] == symbol and
		   self.board[1][1] == symbol and
           self.board[2][2] == symbol: self.status = "Player %s wins!" % upper(symbol)

		if self.board[0][2] == symbol and
		   self.board[1][1] == symbol and
           self.board[2][0] == symbol: self.status = "Player %s wins!" % upper(symbol)

	def makeMove():
		postion = map(int,input().split)
		row = positions[0]
		column = positions[1]
		if self.turn = "Player X":
			self.board[row][column] = 'X'
		else:
			self.board[row][column] = 'O'
		return

def startGame():
	match = Match()
	print(match)
    while(match.status != finished):
		match.makeMove()
		match.checkForW()
	

def menu():
	print("xxx TIC TAC TOE! ooo")
	print("MENU\n")
	print("1: Start Game!\n
		   2: Instructions\n
		   3: Quit")
	option = int(input)
	choices = { 1 : startgame(),
				2 : print(instructions),
				3 : sys.exit()

def main():
	menu()
	
if __name__ == "__main__":
	main()
    
