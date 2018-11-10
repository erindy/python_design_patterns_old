from patterns import factory


if __name__ == '__main__':
    f = factory.ShapeFactory()
    s = f.getShape('square')
    s.draw()