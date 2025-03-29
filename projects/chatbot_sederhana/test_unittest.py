import unittest
from main import *

class Test(unittest.TestCase):
    def test_easy_case(self):
        self.assertEqual(chatbot_respon("hai"), "Halo!, Bagaimana kabarmu hari ini?")
    def test_hard_case(self):
        self.assertEqual(chatbot_respon("jelaskan tentang AGI"), "Maaf, aku belum mengerti pertanyaan itu. Coba tanyakan yang lain!")

if __name__ == "__main__":
    unittest.main()