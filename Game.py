# Import Modules
from Snake import Snake

class Game:
    # Define directions as constants to make them easier to reference.
    DIR_UP = (0, 1)
    DIR_DOWN = (0, -1)
    DIR_RIGHT = (1, 0)
    DIR_LEFT = (-1, 0)
    
    # Integer Values to represent the display characters.
    EMPTY = 0
    BODY = 1
    HEAD = 2
    apple = 3
    
    # Dictionary for Display Characters
    DISPLAY_CHARS = {
        EMPTY: " ",
        BODY: "O",
        HEAD: "X",
        apple: "*"
    }

    # Game Constructor
    def __init__(self, width, height):
        self.height = height
        self.width = width
        
        init_body = [
            (0,0),
            (1,0),
            (2,0),
            (3,0),
            (4,0)
        ]
        
        self.snake = Snake(init_body, self.DIR_UP)

    def _board_matrix(self):
        # Returns a 2D Matrix of None Values to represent the squares.
        matrix = [[self.EMPTY for _ in range(self.height)] for _ in range(self.width)]
        
        # x - 0
        # y - 1
        # Use X and Y coordinates retrieved from a snake to apply them to our board matrix where we will render the border later.
        for coordinates in self.snake.body:
            matrix[coordinates[0]][coordinates[1]] = self.BODY
            
        # Get the value at the head. (type: tuple)
        head = self.snake.head()
        matrix[head[0]][head[1]] = self.HEAD
        
        # TODO: Use this to figure out the apple stuff.
        #
        #
        
        return matrix
    
    # TODO: Find way to print out the board with spaces and a border.
    # Start with the Top - +----+
    def _render(self):
        # Initialize Matrix
        matrix = self._board_matrix()
        
        top_bottom_border = "+" + "-" * self.width + "+"
        
        print(top_bottom_border)
        
        # First I want to switch out the values in the row for the display characters.
        # One thing I didn't realize is that this supposed to go a different direction for it to make sense.
        
        # Essentially going row by row and the x goes through the values in each row.
        # Start off with Y as that is the y-axis is representative to the height.
        for y in range(0, self.height):
            #Start off with the vertical line then add for each line we go through
            line = '|'
            for x in range(0, self.width):
                cell_value = matrix[x][self.height - 1 - y] # TODO: figure out why it is self.height - 1 - y.
                line += self.DISPLAY_CHARS[cell_value]
            line += '|'
            print(line)
                
        print(top_bottom_border)
        #Print Top and Bottom
        #Print Inside of Board as Blank Spots
        
        
        #TODO: Learn how to replace the values that are spaces with position of the 0/X
            
    
game = Game(30, 10)
game._render()