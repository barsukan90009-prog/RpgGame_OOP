from character import Character

class RangedFighter(Character):
    def __init__(self, name: str, damage: int, health: int, weapon: str, typeAttack: str, envasion: int):
        super().__init__(name, damage, health, weapon, typeAttack)
        self.envasion = envasion