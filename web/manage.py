# -*- coding:utf-8 -*-
import re

from flask import Flask, request, render_template, jsonify

from server import socket_server

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.form['data']
        if re.match('[0-9a-fA-F]*$', data):
            socket_server.response_data.appendleft(data.encode())
            return jsonify({'result': 1})
        else:
            return jsonify({'result': 0})
    else:
        try:
            data = socket_server.request_data.pop()
            print('data', data)
            data = data.decode()
            print(data)
        except IndexError:
            data = 0
        return jsonify({'data': data})


if __name__ == '__main__':
    socket_server.run()
    app.run(debug=True, use_reloader=False)
