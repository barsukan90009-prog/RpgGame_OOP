from rangedFighter import RangedFighter

class Archer(RangedFighter):
    def __init__(
        self, 
        name: str, 
        damage: int = 40, 
        health: int = 150, 
        weapon: str = "Лук охотника",
        type_attack: str = "Натягивает титиву и запускает стрелу", #тЕтиву, но название свойства хуевое. Это не тип атаки, а описание
        envasion: int = 30, 
        ammunation: int = 5
    ):
        super().__init__(name, damage, health, weapon, type_attack, envasion)
        self.ammunation = ammunation