from character import Character

class RangedFighter(Character):
    def __init__(
        self, 
        name: str, 
        damage: int, 
        health: int,
        weapon: str, 
        type_attack: str, 
        envasion: int
    ):
        super().__init__(name, damage, health, weapon, type_attack)
        self.envasion = envasion