from weapon import Weapon
class Character():
    def __init__(
        self,
        name: str, 
        base_damage: int, 
        health: int, 
        weapon: Weapon,       
    ):
        self.name = name
        self.base_damage = base_damage
        self.health = health
        self.weapon = weapon
    

