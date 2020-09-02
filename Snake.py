class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        # Will add position to the front of the snake from the back.
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        # Returns the position of the front of the snake's body.
        return self.body[-1]
    