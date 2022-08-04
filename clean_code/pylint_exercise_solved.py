"""Sample Garden module"""
from typing import List, Optional


class Garden:
    """A class implementing a garden."""
    def __init__(self, area: Optional[float] = None):
        self._plants: List[str] = []
        self._area = area

    def get_garden_area(self) -> Optional[float]:
        """Returns an area of a garden.

        :return: Area of garden
        """
        return self._area

    def get_all_plants(self) -> List[str]:
        """
        Returns list of all plants in the garden.
        :return plants: List of plants
        """
        return self._plants

    def add_plant(self, plant: str) -> None:
        """
        Appends given plant to the garden plants list.
        :param plant: plant name
        :return None:
        """
        self._plants.append(plant)


if __name__ == '__main__':
    garden = Garden(10.3)
    print(garden.get_garden_area())
    garden.add_plant("Sunflower")
    print(garden.get_all_plants())
