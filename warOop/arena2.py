# Объявил класс Арена 2
class Arena2:
    # Конструктор класса метод инициализации принимял 2 бойцов
    def __init__(self, fighter1, fighter2):
        # Сохраняет 1 и 2 бойца в атрибуты
        self.fighter1 = fighter1
        self.fighter2 = fighter2
    # Объявлен общий метод атаки принимающий в себя атакующуго и защищающегося
    def makeAttack(self, attacker, defender):
        # Вычитает урон атакующего из хп защищающегося
        defender.health -= attacker.damage
        # Условие если здоровье защищающегося ниже нуля
        if defender.health < 0:
        # то приравниватеся хп = 0
            defender.health = 0
        print(f"{attacker.name} атакует! {defender.name} получает {attacker.damage} урона (Осталось здоровья: {defender.health})")
    # Объявлен метод выполняющий атаку текущего бойца и проверяющий хп защищающегося принимает в себя атакер дефендер
    def make_turn(self, attacker, defender):
        # Вызывает метод атаки чтобы атакер ударил дефендер
        self.makeAttack(attacker, defender)
        # Условие проверяет меньше или равно нулю хп дефендера
        if defender.health <= 0:
            print(f"\nПобедитель: {attacker.name}!")
            #true если бой окончен чей-то гибелью
            return True
        # false если хп не стало меньше либо равным нулю
        return False
    # Объявлен Метод запускающий сам цикл боя
    def startFight(self):
        print(f"Начало дуэли между бойцами {self.fighter1.name} и {self.fighter2.name}!\n")

        # Инициализация счетчика раундов начинается с 1-ого
        roundNum = 1
        # Цикл ограничиващий раунды до 5 включительно
        while roundNum < 5: 
            print(f"--- Раунд {roundNum} ---")
            # Цикл for который меняет атакер на дефендера после удара
            for attacker, defender in [(self.fighter1, self.fighter2), (self.fighter2, self.fighter1)]:
                # Условие в котором проверяется завершился ли бой чей-то победой
                if self.make_turn(attacker, defender):
                    # Если мейктарн возвращает true, то есть бой закончился чей-то победой, то заканчивает метод стартфайт
                    return
            
            print(f"Статус: {self.fighter1.name} [{self.fighter1.health} HP] vs {self.fighter2.name} [{self.fighter2.health} HP]\n")
            # Увеличивает номер раунда на 1 для следующего цикла
            roundNum += 1
            



