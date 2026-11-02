import random
from arena2 import Arena2
from archer import Archer
from assasin import Assasin
from mage import Mage
from varvar import Varvar

# Импортируем сами объекты оружия из weapon.py
from weapon import AXES, BOW, DAGGER, PRIZM_BLOOD, STAFF_MAGIC, SWORD
from witch import Witch

# Создал список бойцов
fighterPool = [
    Witch("Ксения Минетчица"),
    Mage("Виктор Корнеплод"),
    Assasin("Вадя Водяной"),
    Archer("Николло Членовредитель"),
    Varvar("Дрочеслав Сергеевич"),
]

# Рандомный выбор бойца из списка
random.shuffle(fighterPool)

# Выбираем двух бойцов из списка для боя с помощью метода pop(),
# который удаляет и возвращает последний элемент списка
f1 = fighterPool.pop()
f2 = fighterPool.pop()

# Рандомим оружие из созданных объектов
f1.weapon = random.choice([BOW, AXES, DAGGER, PRIZM_BLOOD, SWORD, STAFF_MAGIC])
f2.weapon = random.choice([BOW, AXES, DAGGER, PRIZM_BLOOD, SWORD, STAFF_MAGIC])

# Выводим информацию о выбранных бойцах и их оружии в консоль
print(
    f"Первый боец выбран: {f1.name}. Оружие: {f1.weapon.name}"
    f" ({f1.weapon.description})"
)
print(
    f"Второй боец выбран: {f2.name}. Оружие: {f2.weapon.name}"
    f" ({f2.weapon.description})\n"
)

# Запуск боя
Arena2(f1, f2).start_fight()
