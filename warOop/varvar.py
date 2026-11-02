from nearFighter import NearFighter
from weapon import Weapon

class Varvar(NearFighter):
    def __init__(
        self, name: str, 
        base_damage: int = 30, 
        health: int = 200, 
        weapon: Weapon = None,  
        armour: int = 30, 
        double_attack: int = 60
    ):
        super().__init__(name, base_damage, health, weapon, armour)
        self.double_attack = double_attack