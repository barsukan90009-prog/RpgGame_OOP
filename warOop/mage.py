from rangedFighter import RangedFighter

class Mage(RangedFighter):
    def __init__(
        self, 
        name: str,
        damage: int = 70,
        health: int = 100, 
        weapon: str = "Посох Мерлина", 
        type_attack: str = "Выпускает молнию при взмахе посоха", 
        envasion: int = 30, 
        mana: int = 50
    ):
            super().__init__(name, damage, health, weapon, type_attack, envasion)
            self.mana = mana
