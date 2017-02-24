# -----------------------------------------------------------------------------
# Name:       robot
# Purpose:    class definition for robots
#
# Author:   Roger McClain
# Date:     2/22/2017
# -----------------------------------------------------------------------------

"""
Module to describe and control robot objects in a maze.
"""
import tkinter


class Robot(object):
    """
    This class represents an object that can travel around a maze via move
    commands and has a battery attribute.

    Arguments:
    name (str): THe robots name.
    color (str): The color the robot will appear as.


    Attributes:
    battery (int): The robots fuel to move about.
    row (int): The robots Y position.
    column (int): The robots X position.
    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20
    battery = full

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.recharge()

    def __str__(self):
        return "%s is a %s robot lost in a maze." % \
               (self.name, str.lower(self.color))

    def __gt__(self, other):
        if self.battery > other.battery:
            return True
        else:
            return False

    def recharge(self):
        """
        This function recharges the battery attribute by setting it equal to
        full
        """
        self.battery = self.full
        return self

    def _move(self, rdelta=0, cdelta=0):
        """
        This movement function consolidates checks for valid movements


        Parameters:
        Number of spaces to change either the row or the column.

        :return its self so that we can use method chaining
        """
        if (self.column + cdelta < len(self.maze[1])
        and (self.row + rdelta < len(self.maze[0]))
        and (self.row + rdelta >= 0)
        and (self.column + cdelta >= 0)
        and (self.battery >= 1)
        and (self.maze[self.row + rdelta][self.column + cdelta])):
            self.battery -= 1
            self.row += rdelta
            self.column += cdelta
            print("The robot %s's row position is %s and his "
                  "column position is %s."
                  % (self.name, self.row, self.column))
            return self
        else:
            print('Invalid move! (obstacle in the way or battery too low)')

    def one_step_forward(self):
        """
        This function will call the _move function with an rdelta value of +1
        """
        self._move(rdelta=1)
        return self

    def one_step_back(self):
        """
        This function will call the _move function with an rdelta value of -1
        """
        self._move(rdelta=-1)
        return self

    def one_step_right(self):
        """
        This function will call the _move function with a cdelta value of +1
        """
        self._move(cdelta=1)
        return self

    def one_step_left(self):
        """
        This function will call the _move function with a cdelta value of -1
        """
        self._move(cdelta=-1)
        return self

    def forward(self, steps):
        """
        Calls the appropriate movement function the number of times indicated
        by the by the steps parameter.
        """
        for i in range(0, steps):
            self.one_step_forward()
        return self

    def backward(self, steps):
        """
        Calls the appropriate movement function the number of times indicated
        by the by the steps parameter.
        """
        for i in range(0, steps):
            self.one_step_back()
        return self

    def right(self, steps):
        """
        Calls the appropriate movement function the number of times indicated
        by the by the steps parameter.
        """
        for i in range(0, steps):
            self.one_step_right()
        return self

    def left(self, steps):
        """
        Calls the appropriate movement function the number of times indicated
        by the by the steps parameter.
        """
        for i in range(0, steps):
            self.one_step_left()
        return self

    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


# Enter you UnderwaterRobot Class definition below
class UnderwaterRobot(Robot):
    """
    The second class of Robot, it inherits from "Robot" but also can dive and
    has a depth attribute.

    Arguments:
    name (str): THe robots name.
    color (str): The color the robot will appear as.


    Attributes:
    depth (int): The robots depth.
    row (int): The robots Y position.
    column (int): The robots X position.
    """

    def __init__(self, name, color, depth=0, row=0, column=0):
        self.depth = depth
        super().__init__(name, color, row=row, column=column)

    def __str__(self):
        return "%s is a %s robot diving under water." % \
               (self.name, str.lower(self.color))

    def dive(self, fathoms):
        """
        Adjust the robots depth via this dive function. Will always be a
        positive integer

        """
        self.depth += fathoms
        return self



