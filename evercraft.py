class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character():

    def __init__(self):
        self.name = ''
        self.alignment = Alignment.NEUTRAL

    @property
    def armor_class(self):
        return 10

    @property
    def hit_points(self):
        return 5

class Combat():

    def __init__(self, attacker, defender):
        self.defender = defender

    def resolve(self, roll):
        self.hit = roll >= self.defender.armor_class
