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

	def makeMove():
		pass

def startGame():
	match = Match()
	print(match)
    while(match.status != finished):
		match.makeMove()
	

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
    
