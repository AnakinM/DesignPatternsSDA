# Nested class implementation


class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = 0

    __instance = None

    def __new__(cls):
        if not Singleton.__instance:
            Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance


if __name__ == "__main__":
    x = Singleton()
    print(x.val)
    x.val = 3
    print(x.val)

    y = Singleton()
    print(y.val)

    print(x)
    print(y)
