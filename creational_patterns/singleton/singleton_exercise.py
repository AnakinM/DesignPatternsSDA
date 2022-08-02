class Cake:
    def __init__(self):
        self._name = ""

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


if __name__ == '__main__':
    cake_1 = Cake()
    cake_1.set_name("Jabłecznik")
    cake_2 = Cake()
    cake_2.set_name("Sernik")

    if cake_1.get_name() == cake_2.get_name():
        print("I'm a Singleton!")
    else:
        print("I'm not a Singleton :(")
