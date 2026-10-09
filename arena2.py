class Arena2:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.roundNum = 1

    def makeAttack(self, attacker, defender):
        #Общий метод для удара
        defender.health -= attacker.damage
        if defender.health < 0:
            defender.health = 0

        print(f"{attacker.name} атакует! {defender.name} получает {attacker.damage} урона (Осталось здоровья: {defender.health})")

    def startFight(self):
        print(f"Начало дуэли между бойцами {self.fighter1.name} и {self.fighter2.name}!\n")

        roundNum = 1
        while self.fighter1.health >0 and self.fighter2.health >0 and roundNum!= 5: #принудительно задал 5 раундов    
            print(f"--- Раунд {roundNum} ---")
            #общим методом 1ый бьет второго бойца
            self.makeAttack(self.fighter1, self.fighter2)
            if self.fighter2.health <= 0:
                print(f"\nПобедитель: {self.fighter1.name}!")
                break
            #общий метод для контратаки
            self.makeAttack(self.fighter2, self.fighter1)
            if self.fighter1.health <= 0:
                print(f"\nПобедитель: {self.fighter2.name}!")
                break
            
            print(f"Статус: {self.fighter1.name} [{self.fighter1.health} HP] vs {self.fighter2.name} [{self.fighter2.health} HP]\n")
            roundNum += 1
            



