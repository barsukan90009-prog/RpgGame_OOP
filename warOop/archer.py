from rangedFighter import RangedFighter

class Archer(RangedFighter):
    #   Зачем решил задать целому классу имя по умолчанию? 
    # Чё, дргуих лучников не может быть? А оружие только эльфийское? 
    # Удобно тебе читать параментры в одну строку на этом залупенском маленьком экране мака
    def __init__(
        self, 
        name: str, 
        damage: int = 40, 
        health: int = 150, 
        weapon: str = "Лук охотника", 
        type_attack: str = "Натягивает титиву и запускает стрелу", 
        envasion: int = 30, 
        ammunation: int = 5
    ):
        super().__init__(name, damage, health, weapon, type_attack, envasion)
        self.ammunation = ammunation