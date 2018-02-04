import os
from bottle import route, run, template, static_file

frettirl = [
    {
        'key1':'value1_1',
        'key2':'value2_1',
        'key3':'value3_1',
        'key4':'value4_1'
    },
    {
        'key1':'value1_2',
        'key2':'value2_2',
        'key3':'value3_2',
        'key4':'value4_2'
    }
]
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./myndir')

@route('/b')
def lidurb():
    return template('frettir', frettir1=frettirl)

@route('/')
def index():
    return template('verk3')

@route('/a')
def lidura():
    return template('lidura')
@route('/kt/<kennitala>')
def kt(kennitala):
    return template('kt', kennitala=kennitala)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
