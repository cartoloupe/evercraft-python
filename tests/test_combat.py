from unittest import TestCase
from evercraft import Character
from evercraft import Combat

class TestCombat(TestCase):

    def setUp(self):
        self.attacker = Character()
        self.defender = Character()
        self.subject = Combat(self.attacker, self.defender)

    def test_attacker_misses_when_roll_less_than_armor_class(self):
        self.subject.resolve(5)
        self.assertFalse(self.subject.hit)

    def test_attacker_hits_when_roll_equals_armor_class(self):
        self.subject.resolve(10)
        self.assertTrue(self.subject.hit)

    def test_attacker_hits_when_roll_greater_than_armor_class(self):
        self.subject.resolve(15)
        self.assertTrue(self.subject.hit)

    def test_attacker_does_not_damage_defender_on_miss(self):
        self.subject.resolve(5)
        self.assertEqual(self.defender.hit_points, 5)

    def test_attacker_damages_defender_on_hit(self):
        self.subject.resolve(15)
        self.assertEqual(self.defender.hit_points, 4)

    def test_attacker_doubly_damages_defender_on_critical_hit(self):
        self.subject.resolve(20)
        self.assertEqual(self.defender.hit_points, 3)
