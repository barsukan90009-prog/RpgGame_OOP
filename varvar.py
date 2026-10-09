from nearFighter import NearFighter

class Varvar(NearFighter):
    def __init__(self, name: str = "Дрочеслав", damage: int = 50, health: int = 200, weapon: str = "Топоры мясника", typeAttack: str = "Удар двумя топорами", armour: int = 70, doubleAttack: bool = True):
        super().__init__(name, damage, health, weapon, typeAttack, armour)
        self.doubleAttack = doubleAttack