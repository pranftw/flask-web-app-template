from flask import Flask, url_for, render_template, redirect
from flask_cors import CORS
from config import HOST, PORT, DEBUG, SERVER_NAME, ALLOWED, SECRET_KEY
from db import Session


app = Flask(__name__)
app.config['SERVER_NAME'] = SERVER_NAME
app.config['SECRET_KEY'] = SECRET_KEY
cors = CORS(app, resources={r"/static/*": {"origins": ALLOWED}})


def objs_to_dict(objs):
    objs_list = []
    for obj in objs:
        obj_dict = {}
        for (var,val) in vars(obj).items():
            if(not(var.startswith("_"))):
                obj_dict[var] = val
        objs_list.append(obj_dict)
    return objs_list


if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
