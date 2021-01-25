from flask import Flask
from flask import jsonify
from flask import request
import json
import datetime
import controller.smsController as smsc
from flask import render_template
import socket
from flask_cors import CORS

import sys, getopt
import time
app = Flask(__name__)
CORS(app)

smsControl = smsc.smsController()

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

@app.route('/', methods=['GET'])
def homeroot():
    return jsonify("connected")

@app.route('/api/testConn', methods=['GET'])
def testcon():
    proc = smsControl.testConn()
    return jsonify(proc)

@app.route('/api/send_sms',methods=['POST'])
def send_sms():
    req_data = request.get_json()
    proc = smsControl.send_sms(req_data)

    return jsonify(proc)

@app.route('/api/read_sms',methods=['POST'])
def read_sms():
    req_data = request.get_json()
    proc = smsControl.read_sms(req_data)
    return jsonify(proc)

@app.route('/api/delete_sms',methods=['POST'])
def delete_sms():
    req_data = request.get_json()
    proc = smsControl.delete_sms(req_data)
    return jsonify(proc)

@app.route('/api/rebootModem')
def rebootModem():
    proc = smsControl.rebootDevice()
    return jsonify(proc)


def main(argv):
    ipaddr = IPAddr
    portnum = 20005
    try:
        opts, args = getopt.getopt(argv,"l:p:",["ipchange=","portchange="])
        for opt, arg in opts:
            if opt in ("-l", "--ipchange"):
                ipaddr = arg
            elif opt in ("-p", "--portchange"):
                portnum = arg

        app.run(debug=True, host=ipaddr, port=portnum)
    except Exception as e:
        print(e)
        app.run(debug=True, host=IPAddr, port=20002)
