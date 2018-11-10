from patterns.creational import (
    factory,
    builder,
 prototype,
 singleton,
 borg
)
from patterns.creational import abstract_factory

from patterns.structural import (
facade
)

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

def test_builder():
    d = builder.Director()
    d.setBuilder(builder.JeepBuilder())
    d.getCar()
    d.getCar().specification()


def test_prototype():
    d = builder.Director()
    d.setBuilder(builder.JeepBuilder())

    jeep = d.getCar().specification()

    jeep2 = jeep.clone()

def test_prototype_2():
    p0 = prototype.Point(0,0)
    p0.__str__()
    p1 = p0.clone(1,1)
    p1.__str__()



def test_singleton():
    x = singleton.Singleton()
    x.val = "burger"

    y = singleton.Singleton()
    y.val = "Chips"

    print(x == y)


def test_borg():
    x = borg.Borg()


    y = borg.Borg()


    print(x == y)


def singleton_modules():
    pass



def test_facade():
    c = facade.Car()
    c.turn_key()
    c.jump()
    c.turn_key()



if __name__ == '__main__':
    test_facade()