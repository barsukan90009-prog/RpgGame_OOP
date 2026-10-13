from rangedFighter import RangedFighter

#     Замечания как и в классе Archer
class Mage(RangedFighter):
    def __init__(self, name: str = "Гарри Полупокер", damage: int = 70, health: int = 100, weapon: str = "Посох Мерлина", typeAttack: str = "Выпускает молнию при взмахе посоха", envasion: int = 50, mana: int = 50):
            super().__init__(name, damage, health, weapon, typeAttack, envasion)
            self.mana = mana
