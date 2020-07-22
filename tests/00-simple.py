import unittest

from URI.Encoder import encode, decode

class Test(unittest.TestCase):
  def test_encode(self):
    self.assertEqual(encode("hello world!"), "hello%20world%21")
    self.assertEqual(encode("Francois"), "Francois")
    self.assertEqual(encode("!@#$%^&*()"), "%21%40%23%24%25%5E%26%2A%28%29")

  def test_decode(self):
    self.assertEqual("hello world!", decode("hello%20world%21"))
    self.assertEqual("Francois", decode("Francois"))
    self.assertEqual("!@#$%^&*()", decode("%21%40%23%24%25%5E%26%2A%28%29"))

if __name__ == '__main__':
  unittest.main()
