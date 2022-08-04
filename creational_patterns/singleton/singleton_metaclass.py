"""
Singleton implementation as meta class
"""


class SingletonMeta(type):
    """
    SingletonMeta class
    """

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class Singleton(metaclass=SingletonMeta):  # pylint: disable=too-few-public-methods
    """
    Singleton class
    """

    def __init__(self):
        self.val = 0


if __name__ == "__main__":
    a = Singleton()
    print(a.val)
    a.val = 4
    print(a.val)

    b = Singleton()
    print(b.val)

    print(a)
    print(b)
