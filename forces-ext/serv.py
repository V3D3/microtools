#!/usr/bin/env python

DIR = '/media/hdd/work/forces'

from flask import Flask
from flask import request
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route ('/live')
@cross_origin ()
def is_live ():
    return "OK"

# change these to customize the file saving formats
def cdir (contest):
    return f"{DIR}/{contest}"
def cfile (contest, problemid):
    return f"{DIR}/{contest}/{problemid}.cpp"
def ifile (contest, problemid, index):
    return f"{DIR}/{contest}/{problemid}.{index}.icase"
def ofile (contest, problemid, index):
    return f"{DIR}/{contest}/{problemid}.{index}.ocase"

def open_editor (contest, problemid):
    # put custom editor opening command here
    os.system (f'code {DIR}')
    os.system (f'code {cfile (contest, problemid)}')

    return True

def write_test_case (contest, problemid, index, i, o):
    # put custom test saving customizations here
    i = bytes (i, "utf-8").decode ("unicode_escape")
    o = bytes (o, "utf-8").decode ("unicode_escape")

    with open (ifile (contest, problemid, index), 'w') as f:
        f.write (i)
    
    with open (ofile (contest, problemid, index), 'w') as f:
        f.write (o)

    return True

# copy to add more hooks for different sites, for instance
@app.route ('/problem/<int:contest>/<problemid>', methods = ['POST'])
@cross_origin ()
def fetch_problem (contest, problemid):
    # check if contest dir exists
    if (not os.path.isdir (cdir (contest))):
        os.mkdir (cdir (contest))

    # check if codefile already exists
    if (os.path.isfile (cfile (contest, problemid))):
        # just open it
        open_editor (contest, problemid)
        return "OK"
    
    data = request.json
    
    # fetch problem cases
    cases = data['cases']
    # write cases to files
    for i in range (len (cases)):
        c = cases[i]
        write_test_case (contest, problemid, i, c['i'], c['o'])

    open_editor (contest, problemid)
    return "OK"

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=20000)