import math
import matplotlib.pyplot as plt

def draw_lines(lines, color='blue'):
    for line in lines:
        plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y], color)
    plt.axis('equal')
    plt.show()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def length(self):
        return math.sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)

class Shape:
    def __init__(self, lines):
        self.lines = lines

    def perimeter(self):
        return sum([line.length() for line in self.lines])

    def draw(self):
        draw_lines(self.lines)

    def point_on_perimeter(self, point):
        for line in self.lines:
            if self._is_point_on_line(line, point):
                return True
        return False

    def _is_point_on_line(self, line, point):
        dx_line = line.point2.x - line.point1.x
        dy_line = line.point2.y - line.point1.y
        dx_point = point.x - line.point1.x
        dy_point = point.y - line.point1.y
        cross = dx_line * dy_point - dy_line * dx_point
        if abs(cross) > 1e-6:
            return False
        dot = dx_point * dx_line + dy_point * dy_line
        if dot < 0 or dot > dx_line**2 + dy_line**2:
            return False
        return True

    def __str__(self):
        return f"Shape with perimeter {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height, center):
        self.width = width
        self.height = height
        self.center = center
        half_width = width / 2
        half_height = height / 2
        
        bottom_left = Point(center.x - half_width, center.y - half_height)
        bottom_right = Point(center.x + half_width, center.y - half_height)
        top_right = Point(center.x + half_width, center.y + half_height)
        top_left = Point(center.x - half_width, center.y + half_height)

        lines = [
            Line(bottom_left, bottom_right),
            Line(bottom_right, top_right),
            Line(top_right, top_left),
            Line(top_left, bottom_left),
        ]
        super().__init__(lines)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width}, height {self.height} and center at ({self.center.x}, {self.center.y})"

class Square(Rectangle):
    def __init__(self, side, center):
        super().__init__(side, side, center)
        self.side = side

    def __str__(self):
        return f"Square with side {self.side} and center at ({self.center.x}, {self.center.y})"

class Circle(Shape):
    def __init__(self, radius, center, num_sides=20):
        self.radius = radius
        self.center = center
        self.num_sides = num_sides

        angle = 2 * math.pi / num_sides
        points = [
            Point(
                center.x + math.cos(angle * i) * radius,
                center.y + math.sin(angle * i) * radius
            ) for i in range(num_sides)
        ]
        lines = [Line(points[i], points[(i + 1) % num_sides]) for i in range(num_sides)]
        super().__init__(lines)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def point_on_perimeter(self, point):
        distance_to_center = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)