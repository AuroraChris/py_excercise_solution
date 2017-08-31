# Excercise 20 : Game Board

'''This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by
  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.


This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game. In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

Things to note:

For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). 
To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. 
This is not required, but whichever way you choose to implement this, it should be explained to the player.
Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. 
Then you can use your Python skills to figure out which row and column they want their piece to be in.
Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
Bonus:

For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. 
In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.'''

from unicurses import *
import check_tic_tac_toe

class game_board(object):

    def __init__(self, size=3):
        self.size = size
        self._board = [[0,0,0],[0,0,0],[0,0,0]]
        self._cordnt = ["Not-specified", "Not-specified"]
        self._sign = [" ", "X", "O"]
        self.player = 1


    @property
    def coordinate(self):
        return self._cordnt
    @coordinate.setter
    def coordinate(self, cor):
        if not (isinstance(cor[0], int) and isinstance(cor[1], int)):
            raise ValueError("Please input an integer!")
        if not ((cor[0] in [0,1,2]) and (cor[1] in [0,1,2])):
            raise ValueError("Please input x, y in 0-2!")
        self._cordnt[0] = cor[0]
        self._cordnt[1] = cor[1]
    
    '''def set_board(self, cor):
        self.coordinate = cor
        self._board[self.coordinate[0]][self.coordinate[1]] = self.player
        return self._board'''

    @classmethod
    def draw_board(cls):
        gb = cls()
        rows = range(2, 2*(gb.size+1)+1)
        stdscr = initscr()
        noecho()
        curs_set(True)
        keypad(stdscr, True)
        if __name__ == "__main__":
            addstr('''(Test)This module is only generate the game board!\n
                        Here is the board (3*3 by default) : \n
                        Press Esc to go back to terminal!''')
        else:
            addstr('''Here is the board (3*3 by default) : \n
                      Press Esc to go back to terminal''')
        for row in rows:
            if row % 2 == 0:
                move(row, 5)
                addstr(" ---" * gb.size)
            else:
                move(row, 5)
                addstr(("|   ") * gb.size + "|")
        #another line with in put
        move(2*(gb.size+1)+2, 5)
        addstr("Please enter the position you want to put (e.g. 00 represents row:0 col:0) : ")
        _allowed_input = [ord("0"), ord("1"), ord("2")]
        keylist = []
        rnd = 0
        while True:
            key = getch()
            if (key in _allowed_input):
                addstr(chr(key))
                keylist.append(chr(key))
                if len(keylist) % 2 == 0:
                    gb.coordinate = [int(keylist[0]), int(keylist[1])]
                    keylist.clear()
            # press enter to draw
            if (key == 10):
                move(3 + 2 * gb.coordinate[0], 7 + 4 * gb.coordinate[1])
                if rnd % 2 == 0:
                    gb.player = 1
                else:
                    gb.player = 2
                addstr(gb._sign[gb.player])
                gb._board[gb.coordinate[0]][gb.coordinate[1]] = gb.player
                move(10, 82)
                rnd = rnd + 1
            if check_tic_tac_toe.check(gb._board):
                move(12, 5)
                addstr(check_tic_tac_toe.check(gb._board))
            # press escape key to quit to terminal
            if (key == 27):
                break
        endwin()
if __name__ == "__main__":
    game_board.draw_board()