from dataclasses import dataclass


class Armor:
    def __init__(self, armor: float, description: str, level: int = 1):
        self.armor = armor
        self.level = level
        self.description = description

    def power(self) -> float:
        return self.armor * self.level


armor = Armor(5.2, "Common armor.", 2)
armor.power()
# 10.4
print(armor)
# <__main__.Armor object at 0x7fc4800e2cf8>

#  с применением dataclass: ---------------------


@dataclass
class Armor2:
    armor: float
    description: str
    level: int = 1

    def power(self) -> float:
        return self.armor * self.level


armor = Armor2(5.2, "Common armor.", 2)
armor.power()
# 10.4
print(armor)
# Armor(armor=5.2, description='Common armor.', level=2)
