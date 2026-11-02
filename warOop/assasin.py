from nearFighter import NearFighter
from weapon import Weapon

class Assasin(NearFighter):
      def __init__(
          self,
          name: str,    
          base_damage: int = 20,
          health: int = 130,
          weapon: Weapon = None,
          armour: int = 20, 
          poison_attack: bool = True, 
          damage_poison: int = 40
      ):
         super().__init__(name, base_damage, health, weapon, armour)
         self.poison_attack = poison_attack
         self.damage_poison = damage_poison
