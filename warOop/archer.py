from rangedFighter import RangedFighter
from weapon import Weapon

class Archer(RangedFighter):
    def __init__(
        self, 
        name: str, 
        base_damage: int = 15, 
        health: int = 150, 
        weapon: Weapon = None,
        envasion: int = 30, 
        ammunation: int = 5
    ):
        super().__init__(name, base_damage, health, weapon, envasion)
        self.ammunation = ammunation