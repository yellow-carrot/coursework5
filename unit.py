from abc import ABC, abstractmethod
from random import randint

from classes import UnitClass
from equipment import Armor, Weapon


class BaseUnit(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.stamina
        self.weapon = None
        self.armor = None
        self.is_skill_used = False

    @property
    def hp(self):
        return round(self.hp, 1)

    @property
    def stamina(self):
        return round(self.stamina, 1)

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def equip_armor(self, armor: Armor):
        self.armor = armor

    def _count_damage(self, target):
        damage = self.weapon.damage * self.unit_class.attack
        self.stamina -= self.weapon.stamina_per_hit

        if target.stamina >= target.armor.stamina_per_turn * target.unit_class.stamina:
            target.stamina -= target.armor.stamina_per_turn * target.unit_class.stamina
            damage -= target.armor.defence * target.unit_class.armor

        damage = round(damage, 1)
        target.damage(damage)
        return damage

    def damage(self, damage: float):
        self.hp -= damage

    def use_skill(self, target):
        if self.is_skill_used:
            return 'Навык уже использован.'
        result = self.unit_class.skill.use(self, target)
        self.is_skill_used = True
        return result

    @abstractmethod
    def hit(self, target):
        pass


class PlayerUnit(BaseUnit):
    def hit(self, target: BaseUnit):
        if self.stamina < self.weapon.stamina_per_hit:
            return f'{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости.'

        damage = self._count_damage(target)
        if damage > 0:
            return f'{self.name}, используя {self.weapon.name}, пробивает {target.armor.name} соперника и наносит {damage} урона.'
        return f'{self.name}, используя {self.weapon.name}, наносит удар, но {target.armor.name} соперника его останавливает.'


class ComputerUnit(BaseUnit):
    def hit(self, target: BaseUnit):
        if not self.is_skill_used and self.stamina >= self.unit_class.skill.stamina and randint(0, 100) <= 10:
            return self.use_skill(target)

        if self.stamina < self.weapon.stamina_per_hit:
            return f'{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости.'

        damage = self._count_damage(target)
        if damage > 0:
            return f'{self.name}, используя {self.weapon.name}, пробивает {target.armor.name} соперника и наносит {damage} урона.'
        return f'{self.name}, используя {self.weapon.name}, наносит удар, но {target.armor.name} соперника его останавливает.'
