# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = "#"

# The visual representation of a hallway.
HALL = "."

# The visual representation of a brussels sprout.
SPROUT = "@"

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = "J"
RAT_2_CHAR = "P"


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol: str, row: int, col: int) -> None:
        """ (Rat, str, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.

        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row: int, col: int) -> None:
        """ (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.

        >>> rat = Rat('P', 1, 4)
        >>> rat.set_location(2, 5)
        >>> rat.row
        2
        >>> rat.col
        5
        """

        assert row >= 0
        assert col >= 0

        self.row = row
        self.col = col

    def eat_sprout(self) -> None:
        """ (Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.

        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1

    def __str__(self) -> str:
        """ (Rat) -> str

        Return a string representation of the rat. P at (4, 3)

        >>> rat = Rat('P', 1, 1)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> print(rat)
        P at (1, 1) ate 2 sprouts.
        """

        return "{} at ({}, {}) ate {} sprouts.".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten
        )


class Maze:
    """ A 2D maze. """

    def __init__(self, maze: list, rat_1: Rat, rat_2: Rat) -> None:
        """ (Maze, list of list of str, Rat, Rat) -> NoneType​

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']], \
                Rat('J', 1, 1), \
                Rat('P', 1, 4))
        >>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.num_sprouts_left
        3
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0

        for row in self.maze:
            self.num_sprouts_left += row.count(SPROUT)

    def is_wall(self, row: int, col: int) -> bool:
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                    ['#', '.', '.', '.', '.', '.', '#'], \
                    ['#', '.', '#', '#', '#', '.', '#'], \
                    ['#', '.', '.', '@', '#', '.', '#'], \
                    ['#', '@', '#', '.', '@', '.', '#'], \
                    ['#', '#', '#', '#', '#', '#', '#']], \
                Rat('J', 1, 1), \
                Rat('P', 1, 4))
        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(1, 1)
        False
        """

        return self.get_character(row, col) == WALL

    def get_character(self, row: int, col: int) -> str:
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column. If there is a rat at that location, then its character should be returned rather than HALL.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']], \
            Rat('J', 1, 1), \
            Rat('P', 1, 4))
        >>> maze.get_character(0, 0)
        '#'
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(1, 2)
        '.'
        >>> maze.get_character(1, 4)
        'P'
        >>> maze.get_character(3, 3)
        '@'
        """

        assert 0 <= row < len(self.maze)
        assert 0 <= col < len(self.maze[0])

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol

        return self.maze[row][col]

    def move(self, rat: Rat, row_change: int, col_change: int) -> str:
        """ (Maze, Rat, int, int) -> str

        Move the rat in the given direction, unless there is a wall in the way.

        Also, check for a Brussels sprout at that location and, if present:
            - have the rat eat the Brussels sprout,
            - make that location a HALL, and
            - decrease the value that num_sprouts_left refers to by one.
            - Return True if and only if there wasn't a wall in the way.


        """

        assert row_change == UP or row_change == DOWN or row_change == NO_CHANGE

        assert col_change == LEFT or col_change == RIGHT or col_change == NO_CHANGE

        new_row = rat.row + row_change
        new_col = rat.col + col_change

        if self.is_wall(new_row, new_col):
            return False

        if self.get_character(new_row, new_col) == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left = self.num_sprouts_left - 1

        self.maze[rat.row][rat.col] = HALL

        rat.set_location(new_row, new_col)

        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        return True

    def __str__(self) -> str:
        """ (Maze) -> str

        Return a string representation of the maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']], \
            Rat('J', 1, 1), \
            Rat('P', 1, 4))
        >>> print(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        maze = []

        for row in range(len(self.maze)):
            row_list = []

            for col in range(len(self.maze[0])):
                if row == self.rat_1.row and col == self.rat_1.col:
                    row_list.append(self.rat_1.symbol)
                elif row == self.rat_2.row and col == self.rat_2.col:
                    row_list.append(self.rat_2.symbol)
                else:
                    row_list.append(self.maze[row][col])

            maze.append(row_list)

        maze_str = "\n".join(["".join(row) for row in maze])

        return maze_str + "\n{}\n{}".format(self.rat_1, self.rat_2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
