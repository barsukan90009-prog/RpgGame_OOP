# class Arena:
#     def __init__(self, fighter1, fighter2):            #объяснить различие и привести пример вызова функции и ее объявления
#         self.fighter1 = fighter1
#         self.fighter2 = fighter2
#         self.round1 = 0
#     def startFight(self):
#         print(f"Начинается файт: {self.fighter1.name} против {self.fighter2.name}!\n")   #разобраться для чего f и как называются фигурные скобки исп с f
#                                                                                         #различия между обратной \n и \r и \r\n
#         roundNum = 1
#         Arena()
#         while self.fighter1.health >0 and self.fighter2.health >0 and self.round1!= 5:     # что такое селф.
#             print(f"--- Раунд {roundNum} ---")

#             damage1 = self.fighter1.damage
#             self.fighter2.health -= damage1
#             print(f"{self.fighter1.name} атакует! {self.fighter2.name} получает {damage1} урона (Осталось здоровья: {max(0, self.fighter2.health)})")

#             if self.fighter2.health <= 0:
#                 print(f"\n Победитель: {self.fighter1.name}!")
#                 self.fighter2.health = 200
#                 self.startFight()
#                 break                                                           #предложить упрощение исключив лишние переменные
            
#             damage2 = self.fighter2.damage
#             self.fighter1.health -= damage2
#             print(f"{self.fighter2.name} контратакует! {self.fighter1.name} получает {damage2} урона (Осталось здоровья: {max(0, self.fighter1.health)})")


#             if self.fighter1.health <= 0:
#                 print(f"\n Победитель: {self.fighter2.name}!")
#                 self.fighter1.health = 300
#                 self.startFight()
#                 break

#             print(f"Статус: {self.fighter1.name} [{self.fighter1.health} HP] vs {self.fighter2.name} [{self.fighter2.health} HP]\n")
#             roundNum += 1
#             self.round1 += 1

#              #предложить упрощение исключив лишние переменные
#              #создать файл arena2.py (копия arena.py но отрефакторенная код упрощен)
#              #
             