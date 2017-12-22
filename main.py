class Animal():
    def __init__(self, name, gender, phrase, bio_class):
        self.phrase = phrase
        self.name = name
        self.gender = gender
        self.bio_class = bio_class

    def speak(self):
        class_name = type(self).__name__.lower()
        phrase = '"{}"'.format(self.phrase)
        print('{} the {} says {}'.format(self.name, class_name, phrase))


class Cow(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Moo', 'mammal')


class Goat(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Baaaa', 'mammal')


class Sheep(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Baaaa', 'mammal')


class Pig(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Oink-oink', 'mammal')


class Duck(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Quack', 'bird')

    def speak(self):
        gender = 'he' if self.gender == 'male' else 'she'
        class_name = type(self).__name__.lower()
        phrase = '"{}"'.format(self.phrase)
        print('{} is a {} and {} says {}'.format(self.name, class_name,
                                                 gender, phrase))


class Chicken(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Cock-a-doodle-doo', 'bird')


class Goose(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, 'Quack', 'bird')


if __name__ == '__main__':
    goat1 = Goat('Betty', 'female')
    goat2 = Goat('Jake', 'male')
    duck = Duck('Joe', 'male')
    sheep1 = Sheep('Dolly', 'female')
    sheep2 = Sheep('Paul', 'male')
    sheep3 = Sheep('Lucy', 'female')
