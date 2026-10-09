from rangedFighter import RangedFighter

class Witch(RangedFighter):
    def __init__(self, name: str = "Рыжая шлюха", damage: int = 70, health: int = 180, weapon: str = "Скипетр Лича", typeAttack: str = "Пронзание магией крови", envasion: int = 50, blood: int = 50):
        super().__init__(name, damage, health, weapon, typeAttack, envasion)
        self.blood = blood