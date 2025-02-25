from materials import Material
from random import randrange


class Agent:

    def consume(self, material: Material):
        amount = randrange(50, 15_000)
        if material.total_quantity > amount:
            material.total_quantity -= amount
        return amount

    def produce(self, material: Material):
        amount = randrange(500, 30_000)
        material.total_quantity += amount
        return amount
