"""Snake class of the Snake_game"""
class Details():
    """used to get head, colour, size of the snake"""
    def __init__(self, snake_head, size, colour):
        """used to get values of the snake"""
        self.snake_head = []
        self.snake_head.insert(0, snake_head)
        self.size = size
        self.colour = colour
        self.i = 0
        self.temp = 0

    def get_coordinates(self):
        """return coordinate values"""
        return self.snake_head[self.i-1]

    def get_size(self):
        """ return size of the snake"""
        return self.size

    def get_colour(self):
        """return colour of the snake"""
        return self.colour

class Snake(Details):
    """ implementation of the snake and its management"""
    def __init__(self, snake_head, size, colour):
        """to use values of the Details class in Snake class"""
        super().__init__(snake_head, size, colour)

    def move_up(self):
        """to move the snake upwards"""
        x_cordinate = self.snake_head[0][0]
        y_cordinate = self.snake_head[0][1]
        y_cordinate -= self.size[1]
        val = (x_cordinate, y_cordinate)
        self.snake_head.insert(0, val)

    def move_down(self):
        """to move the snake downwards"""
        x_cordinate = self.snake_head[0][0]
        y_cordinate = self.snake_head[0][1]
        y_cordinate += self.size[1]
        val = (x_cordinate, y_cordinate)
        self.snake_head.insert(0, val)

    def move_left(self):
        """to move the snake to the left"""
        x_cordinate = self.snake_head[0][0]
        y_cordinate = self.snake_head[0][1]
        x_cordinate -= self.size[0]
        val = (x_cordinate, y_cordinate)
        self.snake_head.insert(0, val)

    def move_right(self):
        """to move the snake to the right"""
        x_cordinate = self.snake_head[0][0]
        y_cordinate = self.snake_head[0][1]
        x_cordinate += self.size[0]
        val = (x_cordinate, y_cordinate)
        self.snake_head.insert(0, val)

    def inside_bounds(self, bound1, bound2):
        """ to check snake_headether the snake is inside the drawn rectangle"""
        x_cordinate = self.snake_head[0][0]
        y_cordinate = self.snake_head[0][1]
        if bound2[0] - bound1[0] < self.size[0] or bound2[1] - bound1[1] < self.size[1]:
            return False

        if x_cordinate < bound1[0] or y_cordinate < bound1[1]:
            return False

        if x_cordinate >= bound2[0] or y_cordinate >= bound2[1]:
            return False

        if x_cordinate < bound1[0] or y_cordinate >= bound2[1]:
            return False

        if x_cordinate >= bound2[1] or y_cordinate < bound1[0]:
            return False

        return True

    def check_collision(self, fcor, fsize):
        """to check collision of the snake with any fruit collides with snake"""
        x_cordinate = self.snake_head[0][0]
        y_cordinate = self.snake_head[0][1]
        if x_cordinate == fcor[0] and y_cordinate == fcor[1]:
            return True

        return False

    def check_collision_with_fruit(self, fcor, fsize):
        """to check collision with the fruit"""

        if self.snake_head[0] == fcor:
            return True

        if len(self.snake_head) > self.temp+1:
            self.snake_head.pop()
        return False

    def check_collision_with_self(self):
        """to check collision with snake body"""

        if self.snake_head[0] in self.snake_head[1:]:
            return True

        return False

    def grow(self):
        """to grow the size of snake"""
        self.temp += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.temp:
            self.i += 1
            return self
        self.i = 0
        raise StopIteration
