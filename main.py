import Agent
import articles
from random import randrange
from time import sleep

agent = Agent()
articles = articles.compile_articles()


while True:

    agent.decide(articles)
    wait = randrange(3, 15)

    sleep(wait)
