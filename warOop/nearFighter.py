from character import Character
from weapon import Weapon

class NearFighter(Character):
    def __init__(
        self, 
        name: str, 
        base_damage: int, 
        health: int, 
        weapon: Weapon,  
        armour: int
    ):
        super().__init__(name, base_damage, health, weapon)
        self.armour = armour
