from rangedFighter import RangedFighter

class Witch(RangedFighter):
    def __init__(
        self, 
        name: str, 
        damage: int = 70, 
        health: int = 180, 
        weapon: str = "Скипетр Лича", 
        type_attack: str = "Выпускает магию крови", 
        envasion: int = 40, 
        blood: int = 50
    ):
        super().__init__(name, damage, health, weapon, type_attack, envasion)
        self.blood = blood