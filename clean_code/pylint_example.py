"""Sample Garden module"""
from typing import List, Union, Any


class garden:
    def __init__(self, area: Union[float, None] = None):
        self._plants: List[str] = []
        self._area = area
        self.i_am_useless_here_and_you_can_remove_me

    def get_garden_area(self) -> Union[float, None]:
        return self.pingpong

    def gEt_alL_plAnts(self, teddy_bear: str) -> List[str]:
        """
        Returns list of all plants in the garden.
        :return plants: List of plants
        """
        return self._plants

    def addPlant(self, PLANT: str) -> None:
        """
        Appends given plant to the garden plants list.
        :param plant: plant name
        :return None:
        """
        self._plants.append(PLANT)


if __name__ == '__main__':
    garden = garden(10.3)
    print(garden.get_garden_area())
    garden.addPlant("Sunflower")
    print(garden.gEt_alL_plAnts())