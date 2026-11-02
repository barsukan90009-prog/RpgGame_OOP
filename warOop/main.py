from witch import Witch
from arena2 import Arena2
from mage import Mage
from assasin import Assasin
from archer import Archer
from varvar import Varvar
# Импорт функции рандом(случайный выбор объекта из списка)
import random

# Создал список бойцов
fighterPool = [
    Witch("Ксения Минетчица"), 
    Mage("Виктор Корнеплод"), 
    Assasin("Вадя Водяной"), 
    Archer("Николло Членовредитель"), 
    Varvar("Дрочеслав Сергеевич")
]

# Рандомный выбор бойца из списка через модулем рандом
# перемешивает список операцией shuffle 
random.shuffle(fighterPool)

# Выбор бойца с последующим удалением из списка
# с помощью метода pop()
f1 = fighterPool.pop()
f2 = fighterPool.pop()

print(f"Первый боец выбран: {f1.name}.")
print(f"Второй боец выбран: {f2.name}.\n")

# Запуск боя из класса Арена2 
Arena2(f1, f2).start_fight()

