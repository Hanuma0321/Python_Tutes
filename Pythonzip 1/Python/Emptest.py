import unittest
from uni import Phonbook
class test(unittest.TestCase):
    def test_look(self):
        pb = Phonbook()
        pb.add("Suman","9983625517")
        num = pb.lookup("Suman")
        self.assertEqual("9983625517",num)
