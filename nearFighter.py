from character import Character

class NearFighter(Character):
    def __init__(self, name: str, damage: int, health: int, weapon: str, typeAttack: str, armour: int):
        super().__init__(name, damage, health, weapon, typeAttack)
        self.armour = armour

# в чем отличие метода функции и процедуры
# разобраться в сигнатуре и объявлении функции 
# привести примеры функции и процедуры 
# разобраться что такое "супер"
# разобраться в чем разница суперинит и инит и зачем в функции инит класса нирфайтер вызывается функция инит 1ой строчкой