class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character():

    def __init__(self):
        self.name = ''
        self.alignment = Alignment.NEUTRAL
        self._damage = 0

    @property
    def armor_class(self):
        return 10

    @property
    def hit_points(self):
        return 5 - self._damage

    def damage(self, points):
        self._damage = self._damage + points

class Combat():

    def __init__(self, attacker, defender):
        self.defender = defender

    def resolve(self, roll):
        self.hit = roll >= self.defender.armor_class
        if roll == 20:
            self.defender.damage(2)
        elif self.hit:
            self.defender.damage(1)
