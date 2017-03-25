# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:   Roger McClain
# -----------------------------------------------------------------------------
'''
This module contains a tkinter GUI that plays Tic Tac Toe

The Game class creates a Canvas Frame and background
then calls the TicTac Class to generate the board and handle logic
'''
import tkinter
import random



class Game(tkinter.Frame):
    '''
    This class handles creating the background
    '''

    # Add your class variables if needed here - square size, etc...)

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background='DarkOliveGreen')
        parent.title('Tic Tac Toe')
        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        # Initializing the board
        board = TicTac(self)
        # Register with geometry manager
        board.pack(padx=20, pady=20)


class TicTac(tkinter.Frame):
    '''
    This class contains the logic for the buttons and the game state as well
    as generating all the geometry stuff for display
    '''
    def __init__(self, parent):
        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART', width=30,
                                        command=self.restart)
        restart_button.pack()
        tkinter.Frame.__init__(self, parent, background='black')
        #  Saving the empty game state for victory checks
        self.game_state = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                           (1, 0): 0, (1, 1): 0, (1, 2): 0,
                           (2, 0): 0, (2, 1): 0, (2, 2): 0}
        #  various variables for use in rest of program
        self.human = 'I'
        self.computer = 'O'
        self.turns = 0
        self.display_button = None
        self.cell = {}
        #   Generates the board and the clickable squares
        for row in range(3):
            for column in range(3):
                cell = tkinter.Label(self, background="white", width=20,
                                     height=10, text='')
                cell.bind("<Button-1>", lambda event, column=column, row=row:
                                            self.play(row, column))
                cell.grid(row=row, column=column, padx=1, pady=1)
                self.cell[(row, column)] = cell
                self.game_state[(row, column)] = cell


        # This method is invoked when the user clicks on a square.
    def play(self, row, column):
        """
        Play function handles click events and logic
        :param row: What row has been clicked
        :param column: What column has been clicked
        :return: an updated dictionary and turn counter
        """
        current = self.cell[(row, column)].cget("text")
        if current == "I" or current == "O":    # Checks if valid space
            print("Invalid Move!")
            return
        #   Changes the label of the square to have whoever clicked it
        self.cell[(row, column)].configure(text=self.human, background='red')
        self.game_state[(row, column)] = self.cell[(row, column)]
        self.turns += 1  # Turn counter increments up
        if self.end_game(self.human):
            # Call end_game function for human player
            self.display_button = tkinter.Button(self, width=20,
                          height=10, text='You WIN')
            self.display_button.grid()

            print("you win!")
            return
        if self.turns == 9:
            #   check if maximum moves have been used
            self.display_button = tkinter.Button(text='TIE GAME',
                                            height=10, width=20)
            self.display_button.pack(side='bottom')
            print('Game Over')
            return
        self.ai_turn()

    def end_game(self, owner):
        """
        This function checks to see if the game is over
        :param take the owner of the square that was selected and checks for
        thier victory:
        :return: True if victory, False if not
        """
        #   A whole bunch of victory state checks.. couldn't figure out a
        #   shorter way, but I know there is one
        row, column = 0, 0
        if row == 0 and column == 0 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row + 1, column)].cget("text") == owner:
                if self.game_state[(row + 2, column)].cget("text") == owner:
                    return True
        if column == 0 and row == 0 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row, column + 1)].cget("text") == owner:
                if self.game_state[(row, column + 2)].cget("text") == owner:
                    return True
        if row == 0 and column == 0 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row + 1, column + 1)].cget("text") == owner:
                if self.game_state[(row + 2, column + 2)].cget(
                        "text") == owner:
                    return True
    #   ----------------------------------------------------------------------
        row, column = 0, 1
        if row == 0 and column == 1 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row + 1, column)].cget("text") == owner:
                if self.game_state[(row + 2, column)].cget(
                        "text") == owner:
                    return True

        row, column = 0, 2
        if row == 0 and column == 2 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row + 1, column)].cget("text") == owner:
                if self.game_state[(row + 2, column)].cget(
                        "text") == owner:
                    return True

        row, column = 0, 2
        if row == 0 and column == 2 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row + 1, column - 1)].cget("text") == owner:
                if self.game_state[(row + 2, column - 2)].cget(
                        "text") == owner:
                    return True
    #   ----------------------------------------------------------------------
        row, column = 2, 0
        if row == 2 and column == 0 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row - 1, column + 1)].cget("text") == owner:
                if self.game_state[(row - 2, column + 2)].cget(
                        "text") == owner:
                    return True

        row, column = 1, 0
        if row == 1 and column == 0 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row, column + 1)].cget("text") == owner:
                if self.game_state[(row, column + 2)].cget(
                        "text") == owner:
                    return True

        row, column = 2, 0
        if row == 2 and column == 0 and \
                        self.game_state[(row, column)].cget("text") == owner:
            if self.game_state[(row, column + 1)].cget("text") == owner:
                if self.game_state[(row, column + 2)].cget(
                        "text") == owner:
                    return True

        return False

    def ai_turn(self):
        """
        This function handles the AI's turn after the human selects a square

        :return:
        """
        ai_choice_row = random.randint(0, 2)   # Just randomly chooses a square
        ai_choice_column = random.randint(0, 2)
        #   Checks if square is open or not
        if self.game_state[(ai_choice_row, ai_choice_column)].cget("text")\
                == '':
            # if not assigns it to AI player
            self.game_state[(ai_choice_row, ai_choice_column)].configure(
                text=self.computer, background='blue')
            self.turns += 1  # Turn counter increments up
            # Checks for computers victory
            if self.end_game(self.computer):
                self.display_button = tkinter.Button(text='COMPUTER WINS',
                                             height=10, width=40)
                self.display_button.pack(side='bottom')
                print("Computer wins!")
        # Keeps trying until empty square selected
        else:
            self.ai_turn()

    def restart(self):
        """
        Restart button basically recreates everything, not sure if prior board
        still exists in memory or something though
        :return:
        """
        # This method is invoked when the user clicks on the RESTART button.
        self.display_button.destroy()
        self.game_state = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                           (1, 0): 0, (1, 1): 0, (1, 2): 0,
                           (2, 0): 0, (2, 1): 0, (2, 2): 0}
        self.human = 'I'
        self.computer = 'O'
        self.turns = 0
        self.cell = {}
        for row in range(3):
            for column in range(3):
                cell = tkinter.Label(self, background="white", width=20,
                                     height=10, text='')
                cell.bind("<Button-1>", lambda event, column=column, row=row:
                            self.play(row, column))
                cell.grid(row=row, column=column, padx=1, pady=1)
                self.cell[(row, column)] = cell
                self.game_state[(row, column)] = cell


def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    Game(root).pack()
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()