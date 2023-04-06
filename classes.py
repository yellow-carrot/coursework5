from dataclasses import dataclass
from skills import Skill, FuryKick, PowerfulShot, HolyHeal


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryKick()
)

ThiefClass = UnitClass(
    name='Вор',
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=PowerfulShot()
)

HealerClass = UnitClass(
    name='Лекарь',
    max_health=100.0,
    max_stamina=50.0,
    attack=0.5,
    stamina=0.5,
    armor=2.0,
    skill=HolyHeal()
)

unit_classes = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass,
    HealerClass.name: HealerClass
}
