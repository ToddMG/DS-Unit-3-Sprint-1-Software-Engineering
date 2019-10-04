from random import randint

class Product:
    """
    Class for defining products from ACME Corp
    """

    def __init__(self, name='', price=10, weight=20, fl=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = fl
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """
        Checks the stealability of the Product depending on its price divided by its weight.
        :return: Stealability of a Product object
        """
        calc = self.price/self.weight
        if calc < 0.5:
            return 'Not so stealable...'
        elif 0.5 <= calc < 1.0:
            return 'Kinda stealable.'
        elif calc >= 1.0:
            return 'Very stealable!'
        else:
            return 'Something went wrong...'

    def explode(self):
        """
        Checks the likelihood of a Product to explode
        :return: Explosion result
        """
        calc = self.flammability * self.weight
        if calc < 10:
            return 'Fizzle'
        elif 10 <= calc < 50:
            return '...boom!'
        elif calc >= 50:
            return 'BABOOM!!'
        else:
            return 'Something went wrong...'

class BoxingGlove(Product):
    """
    Subclass of Product
    """

    def __init__(self, name='', price=10, weight=10, fl=0.5):
        super().__init__(name, price, weight, fl)

    def explode(self):
        """
        :return: Explodeability of a glove.
        """
        return '...it\'s a glove.'

    def punch(self):
        """
        Uses glove object to punch depending on its weight
        :return:
        """
        if self.weight < 5:
            return 'That tickles.'
        elif 5 <= self.weight < 15:
            return 'Hey that hurt!'
        elif self.weight >= 15:
            return 'OUCH!'
        else:
            return 'Something went wrong...'