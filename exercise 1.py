class Soldier:

    rank = 'private'
    weapon = 'AK-74'
    age = 18

    def __init__(self, rank, weapon, age):
        self.rank = rank
        self.weapon = weapon
        self.age = age

    def info(self):
        print(f"Звание: {self.rank}\nОружие: {self.weapon}\nВозраст: {self.age}")

private = Soldier(rank="Private", weapon="AK-74", age=18)
private.info()