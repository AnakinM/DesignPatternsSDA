import copy


class Car:
    # engine_type: petrol, diesel, gas, electric
    def __init__(self, wheels_count: int, doors_count: int, brand: str = "",
                 model: str = "", color: str = "", engine_type: str = ""):
        self._wheels_count = wheels_count
        self._doors_count = doors_count
        self._brand = brand
        self._model = model
        self._color = color
        self._engine_type = engine_type

    @property
    def wheels_count(self) -> int:
        return self._wheels_count

    @wheels_count.setter
    def wheels_count(self, value: int) -> None:
        self._wheels_count = value

    @property
    def doors_count(self) -> int:
        return self._doors_count

    @doors_count.setter
    def doors_count(self, value: int) -> None:
        self._doors_count = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        self._brand = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    @property
    def engine_type(self) -> str:
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value: str) -> None:
        self._engine_type = value

    def clone(self):
        return copy.copy(self)

    def __str__(self):
        return f"Car: {self.color} {self.brand} with " \
               f"{self.engine_type} engine, {self.doors_count} doors and " \
               f"{self.wheels_count} wheels."


class CarManager:
    _base_car = Car(4, 5)

    @staticmethod
    def create_car_with_color(brand: str, model: str, color: str,
                              engine_type: str) -> Car:
        base_car_clone = CarManager._base_car.clone()
        base_car_clone.brand = brand
        base_car_clone.model = model
        base_car_clone.color = color
        base_car_clone.engine_type = engine_type
        return base_car_clone


if __name__ == '__main__':
    car_1 = CarManager.create_car_with_color('Audi', 'A4', 'Pink', 'petrol')
    car_2 = CarManager.create_car_with_color('Honda', 'Civic', 'Aquamarine',
                                             'electric')

    print(car_1)
    print(car_2)

