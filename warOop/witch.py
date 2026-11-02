from rangedFighter import RangedFighter
from weapon import Weapon

class Witch(RangedFighter):
    def __init__(
        self, 
        name: str, 
        base_damage: int = 10, 
        health: int = 180, 
        weapon: Weapon = None,  
        envasion: int = 40, 
        blood: int = 50
    ):
        super().__init__(name, base_damage, health, weapon, envasion)
        self.blood = blood