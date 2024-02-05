class Point: # Classes are named using the PascalCase unlike variables which use camelCase
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.move()
# print(point2.x) AttributeError: point2 has no attribute named x


# An object is an instance of a class
# A class is a blueprint/template for creating objects

