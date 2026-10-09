from rangedFighter import RangedFighter

class Archer(RangedFighter):
    def __init__(self, name: str = "Властелин гей лука", damage: int = 40, health: int = 150, weapon: str = "Эльфийский лук", typeAttack: str = "Натянул титиву и запускает стрелу", envasion: int = 70, ammunation: int = 5):
        super().__init__(name, damage, health, weapon, typeAttack, envasion)
        self.ammunation = ammunation