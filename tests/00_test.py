from uri.encoder import encode, decode

def test_encode(self):
  assert encode("hello world!") == "hello%20world%21"
  assert encode("Francois") == "Francois"
  assert encode("!@#$%^&*()") == "%21%40%23%24%25%5E%26%2A%28%29"

def test_decode(self):
  assert "hello world!" == decode("hello%20world%21")
  assert "Francois" == decode("Francois")
  assert "!@#$%^&*()" == decode("%21%40%23%24%25%5E%26%2A%28%29")

if __name__ == '__main__':
  test_encode()
  test_decode()
