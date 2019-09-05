from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route('/')
def sanitize():
    new_input = request.args.get('input', '')
    return make_response('Your input is ' + escape(new_input))
