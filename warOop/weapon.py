class Weapon:

  def __init__(self, name: str, damage_bonus: int, description: str):
    self.name = name
    self.damage_bonus = damage_bonus  # Сколько урона добавляет
    self.description = description  # Описание атаки

BOW = Weapon(
    name = "Лук охотника",
    damage_bonus = 40,
    description = "Атакует выпуская стрелу из лука" 
)

AXES = Weapon(
    name = "Топоры мясника",
    damage_bonus = 40,
    description = "Атакует двумя топорами" 
)

DAGGER = Weapon(
    name = "Кортик убийцы",
    damage_bonus = 45,
    description = "Атакует со спины" 
)

PRIZM_BLOOD = Weapon(
    name = "Призма крови",
    damage_bonus = 50,
    description = "Атакует Пронзая врага кровью" 
)

SWORD = Weapon(
    name = "Ржавый меч лоха",
    damage_bonus = 20,
    description = "Атакует взмахом меча" 
)

STAFF_MAGIC = Weapon(
    name = "Посох мага",
    damage_bonus = 45,
    description = "Атакует выпуская молнию из посоха" 
)


