import unittest
from main import cost_training_model

class Test(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(cost_training_model(8, 2.50, 8, 7), (56, 140, 1120.0))

if __name__ == '__main__':
    # cost_training_model(8, 2.50, 8, 7)
    unittest.main()