from rangedFighter import RangedFighter
from weapon import Weapon

class Mage(RangedFighter):
    def __init__(
        self, 
        name: str,  
        base_damage: int = 10,
        health: int = 100, 
        weapon: Weapon = None, 
        envasion: int = 30, 
        mana: int = 50
    ):
            super().__init__(name, base_damage, health, weapon, envasion)
            self.mana = mana
