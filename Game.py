# Import Modules
from Snake import Snake


class Game:
    # Define directions as constants to make them easier to reference.
    DIR_UP = (0, 1)
    DIR_DOWN = (0, -1)
    DIR_RIGHT = (1, 0)
    DIR_LEFT = (-1, 0)
    DIR_DIAGONALLY_UP_LEFT = (-1, 1)
    DIR_DIAGONALLY_DOWN_RIGHT = (1, -1)
    EMPTY = 0
    BODY = 1
    HEAD = 2
    apple = 3
    
    # Dictionary for Display Characters
    DISPLAY_CHARS = {
        BODY: 'O',
        HEAD: 'X',
        apple: '*'
    }

    # Game Constructor
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        init_body = [
            (0,0),
            (1,0),
            (2,0),
            (3,0),
        ]
        
        self.snake = Snake(init_body, self.DIR_UP)

    def board_matrix(self):
        # Returns a 2D Matrix of None Values to represent the squares.
        matrix = [[self.EMPTY for _ in range(self.height)] for _ in range(self.width)]
        
        # Use X and Y coordinates retrieved from a snake to apply them to our board matrix where we will render the border later.
        for coordinates in self.snake.body:
            matrix[coordinates[0]][coordinates[1]] = self.BODY
            
        # Get the value at the head. (type: tuple)
        head = self.snake.head()
        matrix[head[0]][head[1]] = self.HEAD
        return matrix
    
    # TODO: Find way to print out the board with spaces and a border.
    # Start with the Top - +----+
    def render(self):
        # Initialize Matrix
        matrix = self.board_matrix()
        
        top_bottom_border = "+" + "-" * self.width + "+"
        
        print(top_bottom_border)
        
        # First I want to switch out the values in the row for the display characters.
        for x in range(0, self.height):
            line = '|'
            for y in range(0, self.width):
                cell_value = matrix[x][y]
                
        print(top_bottom_border)
        #Print Top and Bottom
        #Print Inside of Board as Blank Spots
        
        
        #TODO: Learn how to replace the values that are spaces with position of the 0/X
            
    
game = Game(5, 5)
game.render()