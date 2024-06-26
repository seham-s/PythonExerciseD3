import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

    def slope(self):
        try:
            return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
        except ZeroDivisionError:
            return None  # Can return 'inf' or raise an exception if you prefer

    def point_on_line(self, point):
       
        m = self.slope()
        if m is None and self.point1.x == point.x:  # Vertical line
            return True
        elif m is None:
            return False
        b = self.point1.y - m * self.point1.x
        # Now let's check if the point satisfies the line equation
        return math.isclose(point.y, m * point.x + b)

    def __str__(self):
        return f"Line between ({self.point1.x}, {self.point1.y}) and ({self.point2.x}, {self.point2.y})"


point1 = Point(0, 0)
point2 = Point(3, 4)
point3 = Point(1, 1)  
point4 = Point(2, 3)  

line = Line(point1, point2)

# Print the line's length, slope, and whether point3 and point4 are on the line
print(f"Length of the line: {line.length()}")
print(f"Slope of the line: {line.slope()}")
print(f"Is point3 on the line? {line.point_on_line(point3)}")
print(f"Is point4 on the line? {line.point_on_line(point4)}")

# Print the line representation
print(line)