"""
 The Singleton pattern ensures that a class has only one instance, and provide
 a global point of access to it, for example, a logging class
 
 The Borg idiom (a.k.a monostate pattern) lets a class have as many instances
 as one likes, but ensures that they all share the same state.
 
 __new__ is the first step of instance creatiom, it's called before __init__, 
 and is responsible for returning a new instance of your class.
 __init__ doesn't return anything; it's only responsible for initializing the 
 instance after it's been created.
 
 
 Python modules are singletons
"""

class Singleton:
    __instance = None

    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)

        Singleton.__instance.val = val
        return Singleton.__instance
