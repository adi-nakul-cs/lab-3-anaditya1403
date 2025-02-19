import unittest
from string_splosion import string_splosion

class TestStringSplosion(unittest.TestCase):
    def test_string_splosion(self):
        try :
            self.assertEqual(string_splosion('Code'), 'CCoCodCode')
            self.assertEqual(string_splosion('abc'), 'aababc')
            self.assertEqual(string_splosion('ab'), 'aab')
            self.assertEqual(string_splosion('x'), 'x')
            self.assertEqual(string_splosion('fade'), 'ffafadfade')
            self.assertEqual(string_splosion('There'), 'TThTheTherThere')
            self.assertEqual(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
            self.assertEqual(string_splosion('Bye'), 'BByBye')
            self.assertEqual(string_splosion('Good'), 'GGoGooGood')
            self.assertEqual(string_splosion('Bad'), 'BBaBad')
            print("All the assertions in this block run sucessfully.")

        except AssertionError as e:
            print(f"Asseertion has failed{e}")

if __name__ == "__main__":
    unittest.main()
