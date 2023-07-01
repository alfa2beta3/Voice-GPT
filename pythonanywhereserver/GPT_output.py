from flask import Flask, jsonify,request
import json
import server

app = Flask(__name__)

@app.route('/user', methods = ['GET','POST'])

def index():
    global response

    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf8'))
        input = request_data['text']
        #response = f'I would say {message}'
        response = server.process(input)
        print(response)
        return ""

    if request.method == 'GET':
        return jsonify({'message': response})

if __name__ == "__main__":#if this script is the top-level script
    app.run(debug = True) #dont have to shut down server everytime

