class ShapeInterface:
    def draw(self): pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory:

    # static method no need to pass the self instance
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()

        if type == 'square':
            return Square()

        assert 0, 'Could not find the shape ' + type
