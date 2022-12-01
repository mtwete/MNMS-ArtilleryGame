import unittest
from unittest.mock import MagicMock
from target import Target, TargetAttr

class TestTarget(unittest.TestCase):
    def test_constructor(self):
        target = Target()
        self.assertIsNotNone(target)
        self.assertGreater(target.points, 0)

    def test_targets_are_random(self):
        target1 = Target()
        target2 = Target()
        #assert that the (x, y) coordinates are not the same
        self.assertNotEqual((target1.rect.x, target1.rect.y), (target2.rect.x, target2.rect.y))


    def test_random_creation(self):
        points_list = set(())
        for i in range(5):
            points_list.add(Target().points)
        self.assertGreater(len(points_list), 1)

    def test_all_attributes_match_named_attribute_set(self):
        target = Target()
        target_attr_tuple = TargetAttr[f"{target.name}"]
        self.assertEqual(target.rect.width, target_attr_tuple.width)
        self.assertEqual(target.rect.height, target_attr_tuple.height)
        self.assertEqual(target.points, target_attr_tuple.points)
