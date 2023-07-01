from flask import Flask, jsonify
import server

app = Flask(__name__)

@app.route('/user')

def index():
    response = server.answer
    return jsonify({'message': response})

if __name__ == "__main__":#if this script is the top-level script
    app.run(debug = True) #dont have to shut down server everytime