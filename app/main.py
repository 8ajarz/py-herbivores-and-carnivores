from __future__ import annotations


class Animal_desc():

    def __init__(self) -> None:
        self.creatures = []

    def __set__(self, instance, value):
        self.creatures = value

    def __get__(self, instance, owner):
        return self

    def add_creature(self, obj) -> None:
        self.creatures.append(obj)

    def __str__(self):
        return str([
            {
                "Name": creature.name,
                "Health": creature.health,
                "Hidden": creature.hidden
            }
            for creature in self.creatures
        ])

    def __len__(self) -> int:
        return len(self.creatures)

    def __getitem__(self, index):
        return self.creatures[index]

    def __iter__(self):
        return iter(self.creatures)

    def remove_creature(self, obj) -> None:
        self.creatures.remove(obj)


class Animal:
    alive = Animal_desc()

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.__dict__['alive'].add_creature(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                for indx, creature in enumerate(Animal.alive):
                    if creature is other:
                        Animal.alive.remove_creature(creature)


if __name__ == "__main__":
    pass