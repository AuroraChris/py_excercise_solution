# Excercise 20 : Tic Tac Toe Check

'''This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diaggonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
'''
def check(game=[[],[],[]]):
    diag = 0
    vdiag = 2
    for row in game:
        if (row[0] == row[1] and row[1] == row[2] and row[0] != 0):
            return "Player {0} is winning".format(row[0])
    for col in range(3):
        if (game[0][col] == game[1][col] and game[1][col] == game[2][col] and game[0][col] != 0):
            return "Player {0} is winning".format(game[0][col])
    if (game[0][vdiag] == game[1][vdiag-1] and game[1][vdiag-1] == game[2][vdiag-2] and game[0][vdiag] != 0):
        return "Player {0} is winning".format(game[0][vdiag])
    if (game[diag][diag] == game[diag+1][diag+1] and game[diag+1][diag+1] == game[diag+2][diag+2] and game[diag][diag] != 0):
        return "Player {0} is winning".format(game[diag][diag])
    
    return 0
if __name__ == "__main__":
    print("This is a separate test!")
    print(check([[1, 2, 1],
	            [0, 1, 0],
	            [1, 2, 1]]))