import unittest
import json
from app import app

class BooksApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_books(self):
        response = self.app.get('/books')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_single_book(self):
        response = self.app.get('/books/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], 1)

    def test_create_book(self):
        new_book = {'title': 'Brave New World', 'author': 'Aldous Huxley'}
        response = self.app.post('/books', data=json.dumps(new_book), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['title'], 'Brave New World')

    def test_update_book(self):
        updated_book = {'title': 'Brave New World', 'author': 'Aldous Huxley'}
        response = self.app.put('/books/1', data=json.dumps(updated_book), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Brave New World')

    def test_delete_book(self):
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 204)

    def test_book_not_found(self):
        response = self.app.get('/books/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
