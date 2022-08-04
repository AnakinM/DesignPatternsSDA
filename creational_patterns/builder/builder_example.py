from abc import ABC, abstractmethod
from typing import Optional


class HouseTemplate(ABC):
    @abstractmethod
    def set_walls(self, walls: str) -> None:
        pass

    @abstractmethod
    def set_roof(self, roof: str) -> None:
        pass

    @abstractmethod
    def set_interior(self, interior: str) -> None:
        pass

    @abstractmethod
    def set_basement(self, basement: str) -> None:
        pass


class House(HouseTemplate):
    def __init__(self):
        self._walls: str = ""
        self._roof: str = ""
        self._interior: str = ""
        self._basement: str = ""

    def set_walls(self, walls: str) -> None:
        self._walls = walls

    def set_roof(self, roof: str) -> None:
        self._roof = roof

    def set_interior(self, interior: str) -> None:
        self._interior = interior

    def set_basement(self, basement: str) -> None:
        self._basement = basement

    def __str__(self):
        return f"House has: {self._basement}, {self._walls}, {self._roof}, " \
               f"{self._interior}"


class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def build_interior(self) -> None:
        pass

    @abstractmethod
    def build_basement(self) -> None:
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass


class EuropeanHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house = House()

    def build_walls(self) -> None:
        self._house.set_walls("Blank Brick walls")

    def build_roof(self) -> None:
        self._house.set_roof("Roof Tiles roof")

    def build_interior(self) -> None:
        self._house.set_interior("Modern interior")

    def build_basement(self) -> None:
        self._house.set_basement("Concrete basement")

    def get_house(self) -> House:
        return self._house


class AsianHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house = House()

    def build_walls(self) -> None:
        self._house.set_walls("Brick walls")

    def build_roof(self) -> None:
        self._house.set_roof("Wooden roof")

    def build_interior(self) -> None:
        self._house.set_interior("Minimalistic interior")

    def build_basement(self) -> None:
        self._house.set_basement("Concrete basement")

    def get_house(self) -> House:
        return self._house


class CivilEngineer:
    def __init__(self, house_builder: HouseBuilder):
        self._house_builder = house_builder

    def get_house(self) -> House:
        return self._house_builder.get_house()

    def construct_house(self) -> None:
        self._house_builder.build_basement()
        self._house_builder.build_walls()
        self._house_builder.build_roof()
        self._house_builder.build_interior()


if __name__ == "__main__":
    house_type = input("What type of house do you want to build? "
                       "[European|Asian]: ")
    house_builder: Optional[HouseBuilder] = None
    if house_type.lower() == "european":
        house_builder = EuropeanHouseBuilder()
    elif house_type.lower() == "asian":
        house_builder = AsianHouseBuilder()

    engineer = CivilEngineer(house_builder)
    engineer.construct_house()
    house = engineer.get_house()
    print(house)
