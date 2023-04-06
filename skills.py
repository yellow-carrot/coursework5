from abc import ABC, abstractmethod
# from unit import BaseUnit


class Skill(ABC):
    def __init__(self):
        self.user = None
        self.target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina >= self.stamina

    def use(self, user, target) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()

        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryKick(Skill):
    name = 'Свирепый пинок'
    damage = 12.0
    stamina = 6.0

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику.'


class PowerfulShot(Skill):
    name = 'Мощный укол'
    damage = 15.0
    stamina = 5.0

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику.'
