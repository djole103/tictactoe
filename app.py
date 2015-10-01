class Match:
	def __init__(self):
		self.board = [[ ' ' , ' ' , ' '],
            		  [ ' ' , ' ' , ' '],
             		  [ ' ' , ' ' , ' ']]

		self.turn = "Player X"

	def __repr__(self):
		return "repr"

	def __str__(self):
		return "TIC TAC TOE!\nMake your move: %s\n%s\n%s\n%s" % (self.turn,repr(self.board[0]),repr(self.board[1]),repr(self.board[2]))

def main():
	match = Match()
	print(match)

if __name__ == "__main__":
	main()    
