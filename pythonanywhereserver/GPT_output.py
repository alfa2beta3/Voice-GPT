from flask import Flask, jsonify,request
import json
import authentication
import server

global permit

app = Flask(__name__)

@app.route('/auth', methods =  ['GET','POST'])

def index2():
    global permit

    if request.method == 'POST':
        request_data = request.data
        request_data = json.loads(request_data.decode('utf8'))
        password = request_data['text']
        if password == authentication.scrtkey:
            permit = "allowed"
            return ""

    permit = "authentication error"

@app.route('/user', methods = ['GET','POST'])

def index():
    global response

    if permit == "authentication error":
        print (permit)
        return jsonify({'permission': permit})

    if permit == "allowed":
        if request.method == 'POST':
            request_data = request.data
            request_data = json.loads(request_data.decode('utf8'))
            input = request_data['text']
            response = server.process(input)
            # return jsonify({'post status': "post succeed"})

        if request.method == 'GET':
            return jsonify({'message': response})
            # return jsonify({'post status': "get succeed"})

if __name__ == "__main__":#if this script is the top-level script
    app.run(debug = True) #dont have to shut down server everytime