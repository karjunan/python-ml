# app.py

from chroma_setup import setEmbeddings, getResult
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
messages = [
    {"id": 1, "text": "Hello, world!"},
    {"id": 2, "text": "Welcome to Flask!"}
]

@app.route('/messages', methods=['GET'])
def get_messages():
    str = request.args.get('str')
    return jsonify(getResult(str))

@app.route('/messages', methods=['POST'])
def create_message():
    setEmbeddings()
    return jsonify("saved embeddings"), 201

# @app.route('/messages/<str:data>', methods=['GET'])
# def get_message(data):
#     return getResult(data)


# @app.route('/messages/<int:message_id>', methods=['PUT'])
# def update_message(message_id):
#     updated_message = request.get_json()
#     for message in messages:
#         if message['id'] == message_id:
#             message.update(updated_message)
#             return jsonify(message)
#     return jsonify({"error": "Message not found"}), 404

# @app.route('/messages/<int:message_id>', methods=['DELETE'])
# def delete_message(message_id):
#     global messages
#     messages = [msg for msg in messages if msg['id'] != message_id]
#     return '', 204

if __name__ == '__main__':
    app.run(debug=True)
