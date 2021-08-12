from flask import Flask, url_for, render_template, redirect
from flask_cors import CORS
from config import HOST, PORT, DEBUG, SERVER_NAME, ALLOWED, SECRET_KEY


app = Flask(__name__)
app.config['SERVER_NAME'] = SERVER_NAME
app.config['SECRET_KEY'] = SECRET_KEY
cors = CORS(app, resources={r"/static/*": {"origins": ALLOWED}})


if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
