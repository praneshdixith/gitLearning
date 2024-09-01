import unittest
import json
from app import app

class BooksApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.reset_books()

    def reset_books(self):
        # Initialize the books list to a known state
        self.books = [
            {'id': 1, 'title': '1984', 'author': 'George Orwell'}
        ]

    def test_get_all_books(self):
        response = self.app.get('/books')
        print('GET /books response data:', response.data)  # Debugging line
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    # def test_get_single_book(self):
    #     # Ensure the book exists before retrieving
    #     self.reset_books()
    #     response = self.app.get('/books/1')
    #     print('GET /books/1 response data:', response.data)  # Debugging line
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.content_type, 'application/json')
    #     data = json.loads(response.data)
    #     self.assertIsInstance(data, dict)
    #     self.assertEqual(data['id'], 1)

    def test_create_book(self):
        new_book = {'title': 'Brave New World', 'author': 'Aldous Huxley'}
        response = self.app.post('/books', data=json.dumps(new_book), content_type='application/json')
        print('POST /books response data:', response.data)  # Debugging line
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Brave New World')

    # def test_update_book(self):
    #     # Ensure the book exists before updating
    #     self.test_create_book()
    #     updated_book = {'title': 'Brave New World', 'author': 'Aldous Huxley'}
    #     response = self.app.put('/books/1', data=json.dumps(updated_book), content_type='application/json')
    #     print('PUT /books/1 response data:', response.data)  # Debugging line
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.content_type, 'application/json')
    #     data = json.loads(response.data)
    #     self.assertEqual(data['title'], 'Brave New World')

    def test_delete_book(self):
        # Ensure the book exists before deleting
        self.test_create_book()
        response = self.app.delete('/books/1')
        print('DELETE /books/1 response data:', response.data)  # Debugging line
        self.assertEqual(response.status_code, 204)

    def test_book_not_found(self):
        response = self.app.get('/books/999')
        print('GET /books/999 response data:', response.data)  # Debugging line
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()
