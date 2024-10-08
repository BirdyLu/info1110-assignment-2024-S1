from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from typing import Optional, Union

'''
Name:   JIANYI LU
SID:    520400438
Unikey: jilu4724

BoardDisplayer - A helper class used to display the circuit board.
Each time a component is added to the circuit, this board is updated to 
store the component's symbol in its assigned position on the board.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''
component = Union[Emitter, Receiver, Mirror]

class BoardDisplayer:


    def __init__(self, width: int, height: int):
        '''
        Initialises a BoardDisplayer instance given a width and height 
        which is the size of the circuit board. board should be 
        initialised to the return value of the create_board method.

        width:  int             - the width of this board
        height: int             - the height of this board
        board:  list[list[str]] - a list of list of strings representing the 
            circuit board, having the symbol of each 
            component and photon in the circuit at its 
            assigned position

        Parameters
        ----------
        width  - the width to set this board to
        height - the height to set this board to
        '''
        self.width: int = width
        self.height: int = height            
        self.board: list[list[str]] = self.create_board()

    def create_board(self) -> list[list[str]]:
        '''
        Creates a board of size width x height and returns it.

        Returns
        -------
        Returns a list of list of strings representing an empty circuit 
        board of size width x height.

        Example
        ------- 
        >>> self.width, self.height
        (8, 3)
        >>> create_board() # board split across multiple lines for readability
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        The board above has 3 rows (height), with each row having 8 columns (width).
        Each cell is initialised as a space, which represents an empty cell.
        '''
        self.board = []
        i=0
        while i < self.height:
            self.board.append([' ']*self.width)
            i+=1
        return self.board


    def add_component_to_board(self, component) -> None:
        '''
        Adds the symbol of the component on the board at its assigned 
        position.

        Parameters
        ----------
        component: the component to add its symbol on the board

        Hint
        ----------
        You shouldn't need to care what type of component you are adding,
        since all components have a symbol, x and y.
        
        >>> self.board # board split across multiple lines for readability
        [
            [' ', ' ', ' '], 
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        >>> emitter = Emitter('A', 0, 0) Emitter(symbol, x, y)
        >>> receiver = Receiver('R0', 2, 0)
        >>> self.add_component_to_board(emitter)
        >>> self.add_component_to_board(receiver)
        >>> self.board
        [
            ['A', ' ', '0'], 
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]      
        '''
        i = 0
        while i < len(self.board):
            if i == component.y:
                j = 0
                while j < len(self.board[i]):
                    if j == component.x:
                        self.board[i][j] = component.get_symbol()
                    j+=1
            i+=1

    def add_photon_to_board(self, photon: Photon) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Adds the symbol of the photon on the board at its current position. If
        there already is a component on the board at its position, it should not
        replace it.

        Parameters
        ----------
        photon: the photon to add its symbol on the board
        '''
        x = photon.get_x()
        y = photon.get_y()

        if x < self.width and y < self.height and x >= 0 and y >= 0:
            if self.board[y][x] == ' ':
                self.board[y][x] = photon.get_symbol()

    def print_board(self) -> None:
        '''
        Prints a formatted board with the border included.

        Example 1
        ---------
        >>> self.board # board split across multiple lines for readability
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        >>> self.print_board()
        +--------+
        |        |         
        |        |
        |        |
        +--------+

        Example 2
        ---------
        >>> self.board # board split across multiple lines for readability
        [
            ['A', ' ', ' ', ' ', ' ', ' ', ' ', '0'], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['B', ' ', ' ', ' ', ' ', ' ', ' ', '1']
        ]
        >>> self.print_board()
        +--------+
        |A      0|         
        |        |
        |B      1|
        +--------+

        Example 3
        ---------
        >>> self.board # board split across multiple lines for readability
        [
            ['A', '.', '.', '.', '.', '.', '.', '0'], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['B', '.', '.', '.', '.', '.', '.', '1']
        ]
        >>> self.print_board()
        +--------+
        |A......0|         
        |        |
        |B......1|
        +--------+
        '''
        #initialize joined string for return, assign the 1st row of the printed board to the joined string
        joined = '+' + '-'*len(self.board[0]) + '+\n'
        i=0
        while i < len(self.board): 
            joined += '|' + ''.join(self.board[i]) + '|\n'
            i+=1
        #add the last row of the printed board to the joined string
        joined += '+' + '-'*len(self.board[0]) + '+'
        print(joined)