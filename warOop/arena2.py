# Импорт встроенного модуля random для генерации случайных чисел
import random

# Объявлен класс Арена2 представляющий арену для проведения боев между двумя бойцами
class Arena2:

    # # Конструктор класса, который срабатывает при создании объекта Арена2 
    def __init__(self, fighter1, fighter2):

        # # Присвоен переданный аргумент fighter1 в качестве атрибута экземпляра self.fighter1
        self.fighter1 = fighter1

        # # Присвоен переданный аргумент fighter2 в качестве атрибута экземпляра self.fighter2
        self.fighter2 = fighter2

    # Метод для проведения одной конкретной атаки (принимает объект атакующего и защищающегося)
    def make_attack(self, attacker, defender):

        # Получает значение уклонения (envasion) у защищающегося через getattr
        # Если у объекта нет такого атрибута, вернется дефолтное значение 0
        envasion = getattr(defender, "envasion", 0)
        
        # Проверка условия уклонения: если шанс уклонения больше 0, то 
        # выбирается случайное число от 1 до 100 и если оно меньше либо равно значению уклонения, то атака не проходит
        if envasion > 0 and random.randint(1, 100) <= envasion:

            # Правка под объект оружия (.name и .description)
            # Вывод в консоль информации о том, что защищающийся успешно уклонился от атаки.
            print(
                f"{attacker.name} достает {attacker.weapon.name}"
                f" {attacker.weapon.description} {defender.name}...\n"
                f"{defender.name} уклонился от атаки! (шанс был {envasion}%)\n"
                f"Осталось здоровья: {defender.health}\n"
            )

            # Прерываем выполнение метода если защищающийся успешно уклонился от атаки
            return

        # Получаем показатель брони (armour) у защищающегося. Если атрибута нет, возвращается 0
        armour = getattr(defender, "armour", 0)
        
        # Правка: К базовому урону прибавляется damage_bonus объекта оружия
        total_attack_damage = attacker.base_damage + attacker.weapon.damage_bonus

        # Вычисление финального урона: из общего урона вычитаем броню 
        # Функциоальная обертка max(0, ...) гарантирует, что если броня больше урона, итоговое значение не уйдет в минус
        final_damage = max(0, total_attack_damage - armour)
        final_damage = max(0, total_attack_damage - armour)

        # Вычитание итогового урона из текущего здоровья защищающегося
        # Еще один max(0, ...) не дает здоровью опуститься ниже нуля (чтобы не было отрицательных HP)
        defender.health = max(0, defender.health - final_damage)

        # Вывод в консоль подробный лог успешного удара: кто атаковал, каким оружием, 
        # сколько урона прошло с учетом брони и сколько HP осталось   
        print(
            f"{attacker.name} достает из кармана {attacker.weapon.name}. "
            f"{attacker.weapon.description} в {defender.name}"
            f"\n{defender.name} получает {final_damage} урона,"
            f" с учетом брони {armour}\n"
            f"\nОсталось здоровья: {defender.health}\n"
        )

    # Метод, управляющий одним ходом бойца (вызывает атаку и проверяет, не умер ли противник)      
    def make_turn(self, attacker, defender):

        # Вызов метод make_attack для проведения атаки от атакующего к защищающемуся
        self.make_attack(attacker, defender)

        # Проверка условием остатка здоровья меньше либо 0
        if defender.health <= 0:
            print(f"\nПобедитель: {attacker.name}!\n---ХОХЛЫ ПИДОРАСЫ!---")

            # Возвращаем True, сигнализируя, что бой завершен
            return True
        
        # Если здоровье еще есть, возвращаем False (бой продолжается)
        return False

    # Основной метод запускающий цикл боя с выводом имен бойцов
    def start_fight(self):

        # Вывод вступительного сообщения с именами бойцов и их стартовым запасом здоровья
        print(
            f"Начало дуэли между бойцами {self.fighter1.name}"
            f" {self.fighter1.health} HP и {self.fighter2.name}"
            f" {self.fighter2.health} HP!\n"
        )

        # Инициализируем локальную переменную-счетчик раундов, начиная с 1
        round_num = 1

        # Цикл while крутится до тех пор, пока у обоих бойцов здоровье строго больше 0
        while self.fighter1.health > 0 and self.fighter2.health > 0:

            # Вывод шапки текущего раунда в консоль
            print(f"--- Раунд {round_num} ---")

            # Цикл for который меняет атакер на дефендера после удара
            # Расписать что делает конструкция for attacker, defender in [(self.fighter1, self.fighter2), (self.fighter2, self.fighter1)] 
            # Расписать на русском языке, прям словами, прямо по шагам. Нейронку использовать запрещаю. Только документация
            # ЭТО СПИСОК КОРТЕЖЕЙ т.е. его данные нельзя изменить, в данном фрагменте описано
            # что через for перебирает список с присвоением аргументов attacker, defender 
            # к кортежам в списках где в первом и втором ходу бойцы меняются аргументами.

            # Конструкция for пробегает по списку кортежей, меняя местами атакующего и защищающегося в рамках одного раунда
            # Сначала бьет fighter1 по fighter2, затем наоборот (fighter2 по fighter1).
            for attacker, defender in [(self.fighter1, self.fighter2), (self.fighter2, self.fighter1)]:

                # Вызов метода make_turn. Если он возвращает True (кто-то помер)
                if self.make_turn(attacker, defender):

                    # Прерывает цикл for, так как бой завершен
                    return

            # Выводим промежуточный статус здоровья бойцов по итогам завершившегося раунда.
            print(
                f"Статус: {self.fighter1.name} [{self.fighter1.health} HP]"
                f" vs {self.fighter2.name} [{self.fighter2.health} HP]\n"
            )
            # Увеличиваем счетчик раундов на единицу для следующей итерации цикла
            round_num += 1
