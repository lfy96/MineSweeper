import random


class cell(object):
    """
    Initializes each cell in board
        Parameters
            selected : boolean
                Checks if the cell is selected. Default is False
            value : str
                Store the value of each cell. Default is "B", which means blank.
    """
    selected = False
    value = "B"

    def __init__(self):
        self.selected = False

    def __str__(self):
        return str(cell.value)

class board(object):
    def __init__(self, board_row, board_col, num_mines):
        """
        Initializes board
        Parameters
            board_row : int
                    The height of the board
            board_col : int
                    The width of the board
            num_mines : int
                    The number of mines
        Returns
            This function does not return any values.
        Initialize board with mines whose positions are selected randomly.
        The position with mines are set value as "M", which means mines.
        """
        self.board = [[cell() for i in range(board_col)] for j in range(board_row)]
        self.board_row = board_row
        self.board_col = board_col
        self.num_mines = num_mines
        self.selectableSpots = board_row * board_col - num_mines
        n = 0
        while n < num_mines:
            # get an random coordinator to set as mine
            r = random.randint(0, self.board_row - 1)
            c = random.randint(0, self.board_col - 1)
            # if get the coordinator that are used, count minus 1 and get a new random coordinator
            if not self.board[r][c].value == "M":
                self.board[r][c].value = "M"
                n += 1
            else:
                n -= 1

    def __str__(self):
        """
        print board
        Override __str__ method when printed out the object reference it displayed the string which was returned from the __str__ method.
        :return: board(str)
        """
        result = " "
        divider = "\n---"

        for i in range(0, self.board_col):
            result += " | " + str(i)
            divider += "----"
        result += " | "
        divider += "\n"

        result += divider
        for x in range(0, self.board_row):
            result += str(x)
            for y in range(0, self.board_col):
                if self.board[x][y].selected:
                    result += " | " + str(self.board[x][y].value)
                else:
                    result += " |  "
            result += " |"
            result += divider
        return result

    def hitMine(self, x, y):
        """
        update board by using dfs
        :param x: abscissa of click position
        :param y: ordinate of click position
        :return: boolean
        check whether the value of cell is "M"
        if it is, return true
        """
        return self.board[x][y].value == "M"

    def isWinner(self):
        """
        :return: boolean
        check whether there is no position that can be selected
        """
        return self.selectableSpots == 0

    def updateBoard(self, x, y):
        """
        update board by using dfs
        :param x: abscissa of click position
        :param y: ordinate of click position
        :return:
        This function does not return any value.
        """
        #  when hit a mine, return
        if self.board[x][y].value == "M":
            return
        #  use dfs to explore and update the board
        self.dfs(x, y)

    def dfs(self, x, y):
        """
        update board by using dfs
        :param x: abscissa of click position
        :param y: ordinate of click position
        :return:
        This function does not return any value.
        """
        # if click digit, return
        if self.board[x][y].value != "B":
            return
        mine_count = 0
        self.board[x][y].selected = True
        self.selectableSpots -= 1
        # explore eights directions
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for dir in directions:
            curr = x + dir[0]
            curc = y + dir[1]
            if 0 <= curr < self.board_row and 0 <= curc < self.board_col and (not self.board[curr][curc].selected) and self.board[curr][curc].value == "M":
                mine_count += 1
        if mine_count == 0:
            #  if the neighbors of a cell are not mines, set the value of cell as "E", which means Empty
            self.board[x][y].value = "E"
        else:
            # if there are mines in the neighbors, set the value of cell as a digit, which represents the number of mines in its neighbors
            self.board[x][y].value = mine_count
            return
        # explore eight directions
        for dir in directions:
            curr = x + dir[0]
            curc = y + dir[1]
            if 0 <= curr < self.board_row and 0 <= curc < self.board_col and (not self.board[curr][curc].selected):
                self.dfs(curr, curc)






