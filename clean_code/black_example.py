def add(
    variable_1: int,
    variable_2: int,
    variable_3: int,
    variable_4: int,
    variable_5: int,
    variable_6: int,
    variable_7: int,
):
    variable = (
        variable_1 + variable_2 + variable_3 + variable_4 + variable_5 + variable_6
    )
    return variable


extra_long_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

bacon_ipsum_text = "Bacon ipsum dolor amet rump ground round tenderloin sirloin spare ribs shoulder, turducken shankle tongue ham hock jowl flank pork. Drumstick tail shank, spare ribs chicken meatloaf t-bone prosciutto. Short ribs chicken brisket prosciutto capicola. Shankle biltong filet mignon andouille strip steak shank ham hock alcatra."


class Car:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model

    def get_car(self):
        return f"{self._brand} {self._model}"


car = Car("Volkswagen", "Passat")
print(car.get_car())
