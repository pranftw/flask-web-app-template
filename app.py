from flask import Flask, url_for, render_template, redirect
from flask_cors import CORS
from flask import session as flask_session
from config import HOST, PORT, DEBUG, SERVER_NAME, ALLOWED, SECRET_KEY


app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = SERVER_NAME
app.config['SECRET_KEY'] = SECRET_KEY
cors = CORS(app, resources={r"/static/*": {"origins": ALLOWED}})


@app.get("/")
@app.get("/home")
def home():
    return render_template('main.html')


if __name__=='__main__':
    app.jinja_env.cache = {}
    app.run(host=HOST, port=PORT, debug=DEBUG, threaded=True)
