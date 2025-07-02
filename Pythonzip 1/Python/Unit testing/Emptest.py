import unittest
from uni import Phonbook
class test(unittest.TestCase):
    def test_look(self):
        pb = Phonbook()
        pb.add("Bob","12345")
        num = pb.lookup("Bob")
        self.assertEqual(pb.add(1,2),3)
        self.assertEqual("12345",num)
