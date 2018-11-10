from patterns import factory
from patterns import abstract_factory


def test_factory():
    f = factory.ShapeFactory()
    s = f.getShape('square')
    s.draw()


def test_abstract_factory():
    s2 = abstract_factory.Shape2DFactory()
    s2.getShape(1)
    s2.getShape(1).draw()

    s3 = abstract_factory.Shape3DFactory()
    s3.getShape(1).build()



if __name__ == '__main__':
    test_abstract_factory()