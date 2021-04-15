class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.wight = width
        self.height = height

    def get_area(self):
        return "Rectangle (" + str(self.x) + ',' + str(self.y) + ',' + str(self.wight) + ',' + str(self.height) + ")"


rectangle_1 = Rectangle(x=12, y=9, width=100, height=50)

print(rectangle_1.get_area())