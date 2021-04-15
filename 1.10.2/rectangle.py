class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def count_area(self):
        return self.a * self.b


rect_1 = Rectangle(5,2)

print(rect_1.count_area())