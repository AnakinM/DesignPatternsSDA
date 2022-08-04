import random
from typing import List


class Weapon:
    instances = 0

    def __init__(self, name: str, type_: str, damage: int):
        Weapon.instances += 1
        self._name = name
        self._type = type_
        self._damage = damage


class Player:
    def __init__(self, name: str, weapon: Weapon, health: int):
        self._name = name
        self._weapon = weapon
        self._health = health

    def __str__(self):
        return f"{self._name}"


class PlayerFactory:
    weapons = [
        Weapon("AK-47", "Ranged", 20),
        Weapon("Knife", "Melee", 50),
        Weapon("Rocket Launcher", "Ranged", 100),
    ]

    @staticmethod
    def get_player(name: str, health: int = 100):
        return Player(name, random.choice(PlayerFactory.weapons), health)


if __name__ == "__main__":
    players: List[Player] = []
    for i in range(1000):
        players.append(PlayerFactory.get_player(f"Bot_{i}"))

    # for p in players:
    #     print(p)

    print(f"Created {len(players)} players but only {Weapon.instances} weapons")
