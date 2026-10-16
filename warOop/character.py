class Character():
    def __init__(
        self,
        name: str, 
        damage: int, 
        health: int, 
        weapon: str,        # Задача: создать класс "Оружие", чтобы можно было выдать любому из персонажей любое оружие при создании
                            # однако, стоит учесть, что с луком хуево обращается боец ближнего боя, а лучник - отлично
        type_attack: str    # Некорректное применение этого свойства при создании экземпляров класса. Это типа атаки, а не её описание
                            # Если хочешь давать описание, то сделай отдельное поле attackDescription
    ):
        self.name = name
        self.damage = damage
        self.health = health
        self.weapon = weapon
        self.type_attack = type_attack
    

