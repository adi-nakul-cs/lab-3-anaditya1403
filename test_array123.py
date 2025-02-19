import unittest
from array123 import array123

class TestArray123(unittest.TestCase):
    def test_array123_123(self):
        try :
            self.assertEqual(array123([1,1,2,3,1]), True)
            self.assertEqual(array123([1,1,2,4,1]), False)
            self.assertEqual(array123([1,1,2,1,2,3]), True)
            self.assertEqual(array123([1,1,2,1,2]), False)
            self.assertEqual(array123([1,2,3,1,2,3]), True)
            self.assertEqual(array123([1,2,3]), True)
            self.assertEqual(array123([1,1,1]), False)
            self.assertEqual(array123([1,2]), False)
            self.assertEqual(array123([1]), False)
            self.assertEqual(array123([]), False)
            print(f"Success!")
        except AssertionError as e :
            print(f"{e}")

if __name__ == "__main__":
    unittest.main()