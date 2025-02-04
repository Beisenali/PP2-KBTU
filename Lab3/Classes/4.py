import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

point1 = Point(3, 4)
point2 = Point(6, 8)
point1.show()
point1.move(2, 1)
point1.show()
print(f"Distance: {point1.dist(point2)}")
