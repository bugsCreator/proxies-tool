import flask

from class_db import class_db

db = class_db()
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, Request, Response
import requests

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/requestRound')
def requestRound():
    global res
    respose = request.form.to_dict()
    url = respose['url']
    data = db.db_select("working")
    ipData = data[random.randint(0, len(data) - 1)]
    ip = ipData['ip']
    port = ipData['port']
    proxy = {
        'http': f"http://{ip}:{port}",
        'https': f"http://{ip}:{port}"
    }
    error = False
    errorMessage = ""
    try:
        res = requests.get(url, proxies=proxy, timeout=5)
    except Exception as e:

        error = True
        errorMessage = e
        print(e)
    if error:
        return {
            "error": True,
            "Message": errorMessage,
            'statusCode': res.status_code
        }
    return {
        "error": False,
        'statusCode': res.status_code,
        'html': res.text
    }


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
