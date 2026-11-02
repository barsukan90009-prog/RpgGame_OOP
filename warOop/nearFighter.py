from character import Character

class NearFighter(Character):
    def __init__(
        self, 
        name: str, 
        damage: int, 
        health: int, 
        weapon: str, 
        type_attack: str, 
        armour: int
    ):
        super().__init__(name, damage, health, weapon, type_attack)
        self.armour = armour
