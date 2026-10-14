from nearFighter import NearFighter

#     Замечания как и в классе Archer
class Varvar(NearFighter):
    def __init__(
        self, name: str, 
        damage: int = 50, 
        health: int = 200, 
        weapon: str = "Топоры мясника", 
        type_attack: str = "Бьет двумя топорами", 
        armour: int = 30, 
        double_attack: bool = True
    ):
        super().__init__(name, damage, health, weapon, type_attack, armour)
        self.double_attack = double_attack