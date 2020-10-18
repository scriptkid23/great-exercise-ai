# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify,render_template,send_from_directory
from Graph import graphService
from flask_cors import CORS

app = Flask(__name__,static_folder="build/static", template_folder="build")
cors = CORS(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/manifest.json")
def manifest():
    return send_from_directory('./build', 'manifest.json')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./build', 'favicon.ico')

@app.route('/process', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req = request.get_json()
        temp = []
        print(type(req['number_of_disc']))
        for i in range(1,req['number_of_disc'] + 1):
            temp.insert(0,i)
        src=[temp,[],[]]
        dest = [[],[],temp]        
        return jsonify(graphService(src,dest))
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')