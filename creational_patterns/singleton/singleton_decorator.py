# Singleton decorator implementation


def singleton(class_):
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]

    return get_instance


@singleton
class FirstClass:
    def __init__(self):
        self.val = 10


@singleton
class SecondClass:
    def __init__(self):
        self.val = 1


if __name__ == "__main__":
    a = FirstClass()
    a.val = 11
    print(a.val)

    b = FirstClass()
    print(b.val)

    print(a)
    print(b)

    c = SecondClass()
    d = SecondClass()
    print(c)
    print(d)
