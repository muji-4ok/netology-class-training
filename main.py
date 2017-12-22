class Animal:
    mammals = ['Cow', 'Goat', 'Sheep', 'Pig']
    birds = ['Duck', 'Chicken', 'Goose']
    phrase = None

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.class_name = self.__class__.__name__
        if self.class_name in self.mammals:
            self.bio_class = 'mammal'
        elif self.class_name in self.birds:
            self.bio_class = 'bird'

    def speak(self):
        print('{} the {} says "{}"'.format(self.name,
                                           self.class_name.lower(),
                                           self.phrase))


class Cow(Animal):
    phrase = 'Moo'


class Goat(Animal):
    phrase = 'Baaaa'


class Sheep(Animal):
    phrase = 'Baaaa'


class Pig(Animal):
    phrase = 'Oink-oink'


class Duck(Animal):
    phrase = 'Quack'

    def speak(self):
        gender = 'he' if self.gender == 'male' else 'she'
        print('{} is a {} and {} says "{}"'.format(self.name,
                                                   self.class_name.lower(),
                                                   gender, self.phrase))


class Chicken(Animal):
    phrase = 'Cock-a-doodle-doo'


class Goose(Animal):
    phrase = 'Quack'


if __name__ == '__main__':
    goat1 = Goat('Betty', 'female')
    goat2 = Goat('Jake', 'male')
    duck = Duck('Joe', 'male')
    sheep1 = Sheep('Dolly', 'female')
    sheep2 = Sheep('Paul', 'male')
    sheep3 = Sheep('Lucy', 'female')
