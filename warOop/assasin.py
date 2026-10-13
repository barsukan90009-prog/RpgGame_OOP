from nearFighter import NearFighter

#     Замечания как и в классе Archer
class Assasin(NearFighter):
      def __init__(self, name: str = "Отсосин", damage: int = 50, health: int = 130, weapon: str = "Клинок пацанский", typeAttack: str = "Удар изподтишка", armour: int = 70, poisonAttack: bool = True, damagePoison: int = 40):
         super().__init__(name, damage, health, weapon, typeAttack, armour)
         self.poisonAttack = poisonAttack
         self.damagePoison = damagePoison
