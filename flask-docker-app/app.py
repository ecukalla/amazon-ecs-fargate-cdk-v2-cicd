# from flask import Flask, escape, request, render_template
import flask
import datetime
import platform
import os

app = flask.Flask(__name__)


@app.route('/')
def hello():
    name = flask.request.args.get("name", "Flask-demo")
    time = datetime.datetime.now()
    # python_version = platform.python_version()
    # aws_platform = os.environ.get('PLATFORM', 'Amazon Web Services')
    return {"v1": time}


if __name__ == '__main__':
    app.run(
        debug=os.getenv('FLASK_DEBUG',False),
        host='0.0.0.0',
        port=5000
    )
