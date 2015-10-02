import sys

INSTRUCTIONS = "Input position you would like to play in the format \"R C\" where R is the row and C is the column."

class Match:
	def __init__(self):
		self.board = [[ ' ' , ' ' , ' '],
            		  [ ' ' , ' ' , ' '],
             		  [ ' ' , ' ' , ' ']]

		self.players = {0 : "Player X", 1 : "Player O"}
		self.turn = "Player X"
		self.status = "Ongoing"

	def __repr__(self):
		return "repr"

	def __str__(self):
		return "\nMake your move: %s\n%s\n%s\n%s" % (self.turn,repr(self.board[0]),repr(self.board[1]),repr(self.board[2]))

	def checkForW(self):
		if self.turn == 'Player X':
			symbol = 'X'
		else:
			symbol = 'O'
		#horizontally
		if (self.board[0][0] == symbol and 
		    self.board[0][1] == symbol and 
            self.board[0][2] == symbol): self.status = "win"
		if (self.board[1][0] == symbol and 
		    self.board[1][1] == symbol and 
            self.board[1][2] == symbol): self.status = "win"
		if (self.board[2][0] == symbol and 
		    self.board[2][1] == symbol and 
            self.board[2][2] == symbol): self.status = "win"
		#vertical
		if (self.board[0][0] == symbol and 
		    self.board[1][0] == symbol and 
            self.board[2][0] == symbol): self.status = "win"
		if (self.board[0][1] == symbol and 
		    self.board[1][1] == symbol and 
            self.board[2][1] == symbol): self.status = "win"
		if (self.board[0][2] == symbol and 
		    self.board[1][2] == symbol and 
            self.board[2][2] == symbol): self.status = "win"
		#diagonal
		if (self.board[0][0] == symbol and 
	        self.board[1][1] == symbol and 
            self.board[2][2] == symbol): self.status = "win"
		if (self.board[0][2] == symbol and 
		    self.board[1][1] == symbol and 
            self.board[2][0] == symbol): self.status = "win"

	def makeMove(self):
		row, column = None, None
		while(1):
			print("Position you wish to play: ")
			positions = input().split()
			row = int(positions[0])
			column = int(positions[1])
			if (row > 2 or
				row < 0 or
				column > 2 or
				column < 0 or
				self.board[row][column] == 'X' or 
				self.board[row][column] == 'O'):
				print("That is not a playable position. Please play somewhere else.")
				continue
			else:
				break
		if self.turn == "Player X":
			self.board[row][column] = 'X'
		else:
			self.board[row][column] = 'O'
		return

def startGame():
	match = Match()
	movesMade = 0
	while(1):
		if movesMade == 9:
			print("It's a tie!")
			return
		print(match)
		match.makeMove()
		match.checkForW()
		if match.status == "win":
			print("%s wins!" % match.turn)
			return
		else:
			movesMade+=1
			if match.turn == "Player X":
				match.turn = "Player O"
			else:
				match.turn = "Player X"
			
	
def instructions():
	print(INSTRUCTIONS+'\n')
	return

def main():
	choices = { 1 : startGame,
				2 : instructions,
				3 : sys.exit}
	while(1): 
			print("\nxxx TIC TAC TOE! ooo")
			print("MENU\n")
			print("1: Start Game!\n2: Instructions\n3: Quit")
			option = int(input())
			if option not in [1,2,3]:
				print("That option is not an option!")
				continue
			choices[option]()
	
if __name__ == "__main__":
	main()
    
