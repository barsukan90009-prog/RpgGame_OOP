class Character():
    def __init__(self, name: str, damage: int, health: int, weapon: str, typeAttack: str):
        self.name = name
        self.damage = damage
        self.health = health
        self.weapon = weapon
        self.typeAttack = typeAttack
        self.isBusy = False

