from witch import Witch
from arena2 import Arena2
from mage import Mage
from assasin import Assasin
from archer import Archer
from varvar import Varvar
#Импорт функции рандом(случайный выбор объекта из списка)
import random

#Создал список бойцов
fighterPool = [Witch(), Mage(), Assasin(), Archer(), Varvar()]
#Рандомно выбирает бойца(каждая переменная)
f1 = random.choice(fighterPool)
f1.isBusy = True #Флаг*- этот боец уже занят
print(f"Первый боец выбран: {f1.name}.")
#новый список где боец не занят т.е. isBusy = False
fighters = [fighter for fighter in fighterPool if not fighter.isBusy]
f2 = random.choice(fighters)
f2.isBusy = True 
print(f"Боец  {f1.name} уже занят (флаг активен). Выбираем другого из свободных.")
print(f"Второй боец выбран: {f2.name}.\n")
#Начать бой между переменными f1 и f2
Arena2(f1, f2).startFight()
