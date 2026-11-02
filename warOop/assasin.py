from nearFighter import NearFighter

class Assasin(NearFighter):
      def __init__(
          self,
          name: str,    
          damage: int = 50,
          health: int = 130,
          weapon: str = "Клинок пацанский",
          type_attack: str = "Бьет в крысу",
          armour: int = 20, 
          poison_attack: bool = True, 
          damage_poison: int = 40
      ):
         super().__init__(name, damage, health, weapon, type_attack, armour)
         self.poison_attack = poison_attack
         self.damage_poison = damage_poison
