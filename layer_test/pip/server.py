import os
from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = requests.get('https://api.github.com/users/octocat')
    if response.status_code == 200:
        return {'statusCode': 200, 'body': response.json()}
    else:
        return {'statusCode': response.status_code, 'body': 'Error'}
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080)
