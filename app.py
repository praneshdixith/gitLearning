from flask import Flask, jsonify, request, abort

app = Flask(__name__)

app.config['TESTING'] = True

# In-memory data store for books  
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'}
]

@app.route('/books', methods=['GET'])
def get_all_books():
    print('Handling GET /books')  # Debugging line
    return jsonify(books), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    print(f'Handling GET /books/{book_id}')  # Debugging line
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book), 200

@app.route('/books', methods=['POST'])
def create_book():
    print('Handling POST /books')  # Debugging line
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    print(f'Handling PUT /books/{book_id}')  # Debugging line
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    book['title'] = request.json['title']
    book['author'] = request.json['author']
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    print(f'Handling DELETE /books/{book_id}')  # Debugging line
    global books
    books = [b for b in books if b['id'] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
