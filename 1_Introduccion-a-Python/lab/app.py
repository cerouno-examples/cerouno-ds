from flask import Flask
import json 

# Esto trae las funciones de data.py
import data

app = Flask(__name__)

@app.route('/')
def hello_world():
    return json.dumps(data.ethereum())

if __name__ == "__main__":
    app.run()