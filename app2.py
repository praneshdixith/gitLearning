from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Example route testing
#added exampe
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Sample logic for demonstration
    book = {'id': book_id, 'title': 'Sample Book'}
    if book_id == 1:  # Adjust according to your test setup
        return jsonify(book), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

