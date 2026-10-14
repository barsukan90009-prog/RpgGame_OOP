import random
# Объявлен класс Арена2 представляющий арену для проведения боев между двумя бойцами
class Arena2:
    #  Конструктор класса Арена 2 принимающий на вход 2 аргумента
    def __init__(self, fighter1, fighter2):
        # Преобразование 2х аргумернтов в атрибуты класса Арена2
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    # Метод принимающий на вход 2 аргумента класса Арена2
    # Метод инициирует атаку и берет в учет броню защищающегося 
    # и уклонение при промахе прерывает цикл.
    def make_attack(self, attacker, defender,):
        # Использовалась локальная переменная
        envasion = getattr(defender, "envasion", 0)
        if envasion > 0 and random.randint(1,100) <= envasion:
            print(
                f"{attacker.name} достает {attacker.weapon}"
                f" {attacker.type_attack} {defender.name}...\n"
                f"{defender.name} уклонился от атаки! (шанс был {envasion}%)\n"
                f"Осталось здоровья: {defender.health}\n"
            )
            return

        # Выполняет один ход боя: атакующий боец наносит удар защищающемуся,
        # после чего метод вычитает входящий урон атакующего из здоровья защищающегося
        # c учетом его брони(если таковой у объекта нет то вернется 0) и выводит статус боя
        armour = getattr(defender, "armour", 0)
        final_damage = max(0, attacker.damage - armour)
        

            # Args:
                    # attacker: Объект атакующего бойца, который наносит удар.
                    # defender: Объект защищающегося бойца, который получает урон.
                    
        double_attack = getattr(attacker, "double_attack", 0)
        if double_attack > 0 and random.randint(1, 100) <= double_attack:
            final_damage *= 2
            print(
                f"{attacker.name} достает из кармана {attacker.weapon}\n"
                f"{attacker.type_attack} в {defender.name}\n\n"
                f"{defender.name} получает {final_damage} урона,\n"
                f"с учетом брони {armour}\n"
                f"нихуя себе двойная атака шанс был: {double_attack}%\n"
                f"с учетом брони {armour}\n"
            )
        else:
            print(
                f"{attacker.name} достает из кармана {attacker.weapon}\n"
                f"{attacker.type_attack} в {defender.name}\n\n"
                f"{defender.name} получает {final_damage} урона\n"
                f"с учетом брони {armour}\n"
            )

        # 4. обновление здоровья (один раз на весь метод)
        defender.health = max(0, defender.health - final_damage)
        print(f"Осталось здоровья: {defender.health}\n")

        
    # Метод принимающий на вход 2 аргумента
    # Метод проверяет здоровье защищающегося бойца, при выполнении одного из условий
    # либо завершает чьей-то победой либо продолжает.       
    def make_turn(self, attacker, defender):
        self.make_attack(attacker, defender)

        # Проверка условием остатка здоровья меньше либо 0.
        if defender.health <= 0:
            print(f"\nПобедитель: {attacker.name}!")
            return True
        
        return False

        # Returns:
        # bool:
        # True — если здоровье защищающегося <= 0 и бой завершён.
        # False — если защищающийся остался жив и бой продолжается.

    # Метод запускающий цикл боя с выводом имен бойцов
    def start_fight(self):
        print(
            f"Начало дуэли между бойцами {self.fighter1.name}"
            f" {self.fighter1.health} HP и {self.fighter2.name}"
            f" {self.fighter2.health} HP!\n"
        )

        # Инициализация счетчика раундов начинается с 1-ого
        round_num = 1
        # Цикл ограничиващий раунды до 5 включительно
        # А зачем это ограничение? Что будет если я поставлю roundNum < 2? Или обоим бойцам выставлю атаку = 1 --- Раунд не закончится ни чьей победой ибо количество раудов будет меньше 2 принудительно?  
        # (ЗАДАНИЕ ДЛЯ УМНЫХ: ПРОВЕРИТЬ И ПОКАЗАТЬ И НАПИСАТЬ ЧТО КАК И ПОЧЕМУ)

        # self.fighter1.damage = 1
        # self.fighter1.damage = 2

        # Цикл боя длится до момента 0 хп у одного из бойцов,
        # с пошаговой сменой аргументов бойцов из атакующего в защищающего
        # и проверка здоровья с обращением к методу проверки здоровья защищающегося make_turn
        while self.fighter1.health > 0 and self.fighter2.health > 0:
            print(f"--- Раунд {round_num} ---")
            # Цикл for который меняет атакер на дефендера после удара
            # Расписать что делает конструкция  for attacker, defender in [(self.fighter1, self.fighter2), (self.fighter2, self.fighter1)] 
            # Расписать на русском языке, прям словами, прямо по шагам. Нейронку использовать запрещаю. Только документация
            # ЭТО СПИСОК КОРТЕЖЕЙ т.е. его данные нельзя изменить, в данном фрагменте описано
            # что через for перебирает список с присвоением аргументов attacker, defender 
            # к кортежам в списках где в первом и втором ходу бойцы меняются аргументами.

            for attacker, defender in [(self.fighter1, self.fighter2), (self.fighter2, self.fighter1)]:
                
                if self.make_turn(attacker, defender):
                    return
            
            print(
                f"Статус: {self.fighter1.name} [{self.fighter1.health} HP]"
                f" vs {self.fighter2.name} [{self.fighter2.health} HP]\n"
            )
            # Увеличивает номер раунда на 1 для следующего цикла
            round_num += 1
            



