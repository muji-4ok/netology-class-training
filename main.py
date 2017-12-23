class Animal:
    phrase = None

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('{} the {} says "{}"'.format(self.name,
                                           self.__class__.__name__.lower(),
                                           self.phrase))

    def say_class(self):
        print('{} is a {}'.format(self.__class__.__name__,
                                  self.__class__.__base__.__name__.lower()))


class Bird(Animal):
    pass


class Mammal(Animal):
    pass


class Cow(Mammal):
    phrase = 'Moo'


class Goat(Mammal):
    phrase = 'Baaaa'


class Sheep(Mammal):
    phrase = 'Baaaa'


class Pig(Mammal):
    phrase = 'Oink-oink'


class Duck(Bird):
    phrase = 'Quack'

    def speak(self):
        gender = 'he' if self.gender == 'male' else 'she'
        print('{} is a {} and {} says "{}"'.format(
            self.name,
            self.__class__.__name__.lower(),
            gender, self.phrase)
        )


class Chicken(Bird):
    phrase = 'Cock-a-doodle-doo'


class Goose(Bird):
    phrase = 'Quack'


if __name__ == '__main__':
    goat1 = Goat('Betty', 'female')
    goat2 = Goat('Jake', 'male')
    duck = Duck('Joe', 'male')
    sheep1 = Sheep('Dolly', 'female')
    sheep2 = Sheep('Paul', 'male')
    sheep3 = Sheep('Lucy', 'female')
