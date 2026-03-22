import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    d = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    return d <= circle.radius

def rect_in_circle(circle, rect):
    corners = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return all(point_in_circle(circle, c) for c in corners)

def rect_circle_overlap(circle, rect):
    corners = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return any(point_in_circle(circle, c) for c in corners)

c = Circle(Point(150, 100), 75)
