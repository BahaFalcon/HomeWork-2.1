class Monkey:
    max_age = 12
    love_bananas = True

    def __init__(self, age=max_age, food=love_bananas):
        self.age = age
        self.food = food

    def climb(self):
        print("I'm climbing the tree")

chimpanzee = Monkey(age=12, food=True)
chimpanzee2 = Monkey(age=10, food=True)

chimpanzee.climb()
chimpanzee2.climb()