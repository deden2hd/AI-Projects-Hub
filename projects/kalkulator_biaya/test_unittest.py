import unittest
from main import hitung_total_token, hitung_biaya_api, rata_token_per_call

class Test(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(hitung_total_token(5000, 150, 30), 22500000)
        self.assertEqual(hitung_biaya_api(8, 8), 64)
        self.assertEqual(rata_token_per_call(50, 50, 1), 1)

if __name__ == '__main__':
    unittest.main()