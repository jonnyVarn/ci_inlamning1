import app


class AppTester(unittest.TestCase):


    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_message(self):
        response = self.app.get('/')
        message = 'working'
        self.assertEqual(response.data, message)


if __name__ == '__main__':
    unittest.main()
