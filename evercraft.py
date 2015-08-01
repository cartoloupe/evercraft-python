class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character():

    def __init__(self):
        self.name = ''
        self.alignment = Alignment.NEUTRAL
