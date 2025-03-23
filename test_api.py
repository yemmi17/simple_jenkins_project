import unittest
from app import app

class AppTest(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, Jenkins!")

if __name__ == '__main__':
    unittest.main()
