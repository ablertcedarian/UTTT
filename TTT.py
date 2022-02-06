import random
#large portion of implementation borrowed from https://github.com/omegadeep10/tic-tac-toe/blob/master/game.py#L75

boardState = [0]*9

human = "O"
comp = "X"


def checkWin(board):
	winningCombinations = ([[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  			[0, 3, 6], [1, 4, 7], [2, 5, 8],
                  			[0, 4, 8], [2, 4, 6]])

	if (len(checkEmpty(board)) == 0):
		return "Draw"

	for player in (human, comp):
		moveList = getMoves(board, player)
		for moveSet in winningCombinations:
			win = True 
			for position in moveSet:
				if position not in moveList:
					win = False 
			if win:
				return player 

	return False 

def gameOver(board, flag):
	winRes = checkWin(board)

	if winRes != False:
		if flag == 1:
			if winRes== "X":
				print("Game Over. Computer Wins!")
			elif winRes == "O":
				print("Game Over. Human Wins!")
			elif winRes == "Draw":
				print("Game Over. Draw.")
		return True 
	else:
		return False 

def getMoves(board, player):
	moves = []
	for i,n in enumerate(board):
		if n == player:
			moves.append(i)
	return moves 

def checkEmpty(board):
	result = []
	for i,n in enumerate(board):
		if n != human and n != comp:
			result.append(i)
	return result


def minimax(board, depth, player):
	if depth == 0 or gameOver(board, 0):
		winRes = checkWin(board)
		if winRes == comp:
			return 0 
		elif winRes == human:
			return 100 
		else:
			return 50 

	availMoves = checkEmpty(board)

	if player == human:
		toBeat = 0 
		for pos in availMoves:
			board[pos] = player 
			moveVal = minimax(board, depth-1, comp)
			board[pos] = 0 
			toBeat = max(toBeat, moveVal)
		return toBeat 

	if player == comp:		
		toBeat = 100
		for pos in availMoves:
			board[pos] = player 
			moveVal = minimax(board, depth-1, human)
			board[pos] = 0 
			toBeat = min(toBeat, moveVal)
		return toBeat 

def controller(board, depth, player):
	neutral = 50 
	choices = []

	newPlayer = human 
	if player == human:
		newPlayer == comp

	availMoves = checkEmpty(board) 
	for pos in availMoves:
		board[pos] = player 
		moveVal = minimax(board, depth-1, newPlayer)
		board[pos] = 0 

		if moveVal > neutral:
			choices.append([moveVal, pos])
		elif moveVal == neutral:
			choices.append([moveVal, pos])

	choices.sort()
	return choices[0][1]

def printBoard(board):
	print(board[:3])
	print(board[3:6])
	print(board[6:])
	return 0

def main(boardState):
	moveCounter = 0
	printBoard(boardState)

	while gameOver(boardState, 0) == False:
		person_move = int(input("You are O: Choose a number: "))
		boardState[person_move] = "O"
		printBoard(boardState)

		if gameOver(boardState, 1) == True:
			break 

		print("Computer moving")
		engine_move = controller(boardState, -1, "X")
		boardState[engine_move] = "X"
		printBoard(boardState) 

main(boardState)