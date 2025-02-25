from Agent import Agent
from materials import Material
from random import choice, randint, randrange
from time import sleep
from datetime import datetime

agent = Agent()


paprika = Material("PA-021", "Paprika", 3,"Veg")
cucumber = Material("CU-110", "Cucumber", 5, "Veg")
strawberry = Material("STRY-4", "Strawberry", 4, "Fruit")
pear = Material("PE-2", "Pear", 5, "Fruit")
apple = Material("APL-5", "Apple", 3, "Fruit")
salad = Material("SLD-1", "Salad", 1, "Veg")
grapes = Material("GRP-9", "Grape", 2, "Fruit")
avocado = Material("ACO-33", "Avocado", 1, "Veg")


articles = [
    paprika, cucumber, strawberry, pear, apple, salad, grapes, avocado
]

while True:

    selected_material = choice(articles)
    action = randint(0,1)

    if action == 1:
        amount_produced = agent.produce(selected_material)
        print(datetime.now(), "Producing:", selected_material.article_number, amount_produced, selected_material.total_quantity)

    if action == 0:

        previous_amount = selected_material.total_quantity
        amount_consumed = agent.consume(selected_material)

        if previous_amount > amount_consumed:
            print(datetime.now(), "Consuming:", selected_material.article_number, amount_consumed, selected_material.total_quantity)

    wait = randrange(3, 15)

    sleep(wait)
