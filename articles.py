from materials import Material


def compile_articles():

    paprika = Material("PA-021", "Paprika", 3, "Veg")
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

    return articles
