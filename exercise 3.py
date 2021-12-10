class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

    def calculate_age(self, number):
        print(f'Через {number} лет {self.name} исполнится {self.age + number}')


p = Person('Max', 36, 'male')
p.calculate_age(10)