from unittest import TestCase
from evercraft import Character
from evercraft import Alignment
from evercraft import Combat

class TestCharacter(TestCase):

    def setUp(self):
        self.subject = Character()

    def test_name_has_expected_default_value(self):
        self.assertEqual(self.subject.name, '')

    def test_name_can_be_changed(self):
        self.subject.name = 'Bob the Destroyer'
        self.assertEqual(self.subject.name, 'Bob the Destroyer')

    def test_alignment_has_expected_default_value(self):
        self.assertEqual(self.subject.alignment, Alignment.NEUTRAL)

    def test_alignment_can_be_changed_to_good(self):
        self.subject.alignment = Alignment.GOOD
        self.assertEqual(self.subject.alignment, Alignment.GOOD)

    def test_alignment_can_be_changed_to_evil(self):
        self.subject.alignment = Alignment.EVIL
        self.assertEqual(self.subject.alignment, Alignment.EVIL)

    def test_armor_class_has_expected_default(self):
        self.assertEqual(self.subject.armor_class, 10)

    def test_hit_points_has_expected_default(self):
        self.assertEqual(self.subject.hit_points, 5)

    def test_is_alive_when_undamaged(self):
        self.assertTrue(self.subject.alive)

    def test_is_alive_when_damaged(self):
        self.subject.damage(3)
        self.assertTrue(self.subject.alive)

    def test_is_dead_when_out_of_hit_points(self):
        self.subject.damage(5)
        self.assertFalse(self.subject.alive)

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
