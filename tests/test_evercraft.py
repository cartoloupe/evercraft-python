from unittest import TestCase
from evercraft import Character
from evercraft import Alignment

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
