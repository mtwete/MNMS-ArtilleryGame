import unittest
from target import Target, TargetAttr

class TestTarget(unittest.TestCase):
    def test_constructor(self):
        target = Target()
        self.assertIsNotNone(target)
        self.assertGreater(target.points, 0)

    def test_random_creation(self):
        points_list = set(())
        for i in range(10):
            points_list.add(Target().points)
        self.assertGreater(len(points_list), 1)

    def test_all_attributes_match_named_attribute_set(self):
        target = Target()
        target_attr_tuple = TargetAttr[f"{target.name}"]
        self.assertEqual(target.rect.width, target_attr_tuple.width)
        self.assertEqual(target.rect.height, target_attr_tuple.height)
        self.assertEqual(target.points, target_attr_tuple.points)