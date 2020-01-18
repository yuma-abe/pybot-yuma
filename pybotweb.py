from bottle import route, run, template, request,redirect,error
from pybot import pybot
import os

@route('/')
def wrong():
    redirect("/hello")

@route('/hello')
def hello():
    return template('pybot_template', input_text='', output_text='')


@route('/hello', method='POST')
def do_hello():
    input_text = request.forms['input_text']
    input_image = request.files.input_image
    output_text = pybot(input_text, input_image)
    return template('pybot_template', input_text=input_text, output_text=output_text)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

#run(host='localhost', port=8080, debug=True)
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))