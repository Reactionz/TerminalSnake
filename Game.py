# Import Modules
from Snake import Snake

# Define directions as constants to make them easier to reference
UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

class Game:
    # Game Constructor
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0,0), (1,0), (2,0), (3,0)], UP)

    def board_matrix(self):
        # Returns a 2D Matrix of None Values to represent the squares.
        return [[None for i in range(self.height)] for j in range(self.width)]
    
    # TODO: Find way to print out the board with spaces and a border.
    # Start with the Top - +----+
    def render(self):
        # print("Height: " + str(self.height))
        # print("Width: " + str(self.width))
        # Initialize Matrix
        matrix = self.board_matrix()
        width = self.width + 3
        res = ["+" + '-' * width + '+' + '\n']
        #Print Top and Bottom

        
        #Print Inside of Board as Blank Spots
        for i in range(0, len(matrix) - 1):
            res.append('|' + ('' + ' ' * width)[:width] + '|' + '\n')
        res.append('+' + '-'*width + '+')
        print('\n'.join(res))

        #TODO: Learn how to replace the values that are spaces with position of the 0/X
    
game = Game(5, 5)
game.render()