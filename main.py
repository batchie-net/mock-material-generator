from Agent import Agent
from materials import Material

agent = Agent()


paprika = Material("PA-021", "Paprika", "3","Veg")

print(paprika.total_quantity)

agent.produce(paprika)

print(paprika.total_quantity)

agent.consume(paprika)

print(paprika.total_quantity)