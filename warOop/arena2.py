class Arena2:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def makeAttack(self, attacker, defender):
        #Общий метод для удара
        defender.health -= attacker.damage
        if defender.health < 0:
            defender.health = 0
        print(f"{attacker.name} атакует! {defender.name} получает {attacker.damage} урона (Осталось здоровья: {defender.health})")
    #Метод выполняет удар текущего бойца и проверяет хп вторго
    def make_turn(self, attacker, defender):
        self.makeAttack(attacker, defender)
        if defender.health <= 0:
            print(f"\nПобедитель: {attacker.name}!")
            #true если бой окончен чей-то гибелью
            return True
        return False

    def startFight(self):
        print(f"Начало дуэли между бойцами {self.fighter1.name} и {self.fighter2.name}!\n")

        roundNum = 1
        while roundNum < 5: 
            print(f"--- Раунд {roundNum} ---")
            #общим методом 1ый бьет второго бойца и меняются местами(поочередные ходы каждого бойца)
            for attacker, defender in [(self.fighter1, self.fighter2), (self.fighter2, self.fighter1)]:
                if self.make_turn(attacker, defender):
                    return
            
            print(f"Статус: {self.fighter1.name} [{self.fighter1.health} HP] vs {self.fighter2.name} [{self.fighter2.health} HP]\n")
            roundNum += 1
            



