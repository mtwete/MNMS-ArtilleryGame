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
