import unittest
from target import Target, TargetAttr

class TestTarget(unittest.TestCase):
    def test_constructor(self):
        target = Target()
        self.assertIsNotNone(target)
        self.assertGreater(target.points, 0)

    def test_targets_are_random(self):
        target1 = Target()
        target2 = Target()
        self.assertNotEqual(target1.points, target2.points)

if __name__ == '__main__':
    unittest.main()