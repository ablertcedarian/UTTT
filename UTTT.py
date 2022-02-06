#Ultimate Tic Tac Toe Implementation

class UltTicTacToe:
	def __init__(self):
		self.board = [['-']*9]*9
		self.bigBoard = ['-']*9
		self.toPlay = -1 

	def makeMove(self, move, player):
		self.board[move[0]][move[1]] = player

		if self.bigBoard[move[1]] == '' and len(checkEmpty(move[1])) != 0:
			self.toPlay = move[1]
		else:
			self.toPlay = -1 

	def getMoves(self, boardNum, player):
		moves = []
		for i in range(9):
			if self.board[boardNum][i] == player:
				moves.append(i)
		return moves 

	def checkEmpty(self, boardNum):
		moves = []
		for i in range(9):
			if self.board[boardNum][i] == '':
				moves.append(i)
		return moves 

	def checkWin(self):
		combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
		for player in ("X", "O"):
			wins = []
			#check small boards
			for boardNum in range(9):
				moves = getMoves(boardNum, player)
				for combo in combos:
					smallWin = True 
					for position in combo:
						if position not in moves:
							smallWin = False
					if smallWin:
						wins.append(boardNum)
						self.bigBoard[boardNum] = player 

			#check big board
			for combo in combos:
				bigWin = True 
				for position in combo:
					if position not in wins:
						bigWin = False 
				if bigWin:
					return player 

		#check draw
		boardsLeft = []
		for i in range(9):
			if self.bigBoard[i] == '':
				boardsLeft.append(i)
		if len(boardsLeft) == 0:
			return "Draw"

		return False 

	def gameOver(self):
		if self.checkWin != False:
			return True
		return False 

	def printBoard(self):
		#print board
		for row in range(1, 10):
			row_str = ["|"]
			for col in range(1, 10):
				i = ((row - 1) % 3) * 3 + ((col - 1) % 3)
				row_str += [str(self.board[int(row/3) + int(col/3)][i])]
				if (col) % 3 == 0:
					row_str += ["|"]
			if (row-1) % 3 == 0:
				print("-"*(len(row_str)*2-1))
			print(" ".join(row_str))
		print("-"*(len(row_str)*2-1))    	

	def printBig(self):
		#print big board 
		for row in range(0, 3):
			row_str = ["|"]
			for col in range(0, 3):
				row_str += [str(self.bigBoard[row + col])]
				row_str += ["|"]
			print("-"*(len(row_str)*2-1))
			print(" ".join(row_str))
		print("-"*(len(row_str)*2-1))  		


game = UltTicTacToe()
game.printBoard()
game.printBig()