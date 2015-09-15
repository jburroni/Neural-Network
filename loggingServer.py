import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

filename = 'firing_log.txt'
confile = "connections.txt"
conwfile = "connections_wieghts.txt"
fileC = None
fileCW = None

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route('/logging', methods=['POST'])
def log():
    log = request.get_json()
    write(log)
    return "success"

@app.route('/connection', methods=['POST'])
def logConnections():
    log = request.get_json()
    #if(fileC == None):
    	#openFC()
    #writeCon(fileC, log)
    writeCon(confile, log)
    return "success"

@app.route('/conweights', methods=['POST'])
def logWeights():
    log = request.get_json()
    #if(fileCW == None):
    	#openFCW()
    #writeCon(fileCW, log)
    writeCon(conwfile, log)
    return "success"

@app.route('/c_close', methods=['POST'])
def closeConLogging():
	closeFC()
	return "success"
	
@app.route('/cw_close', methods=['POST'])
def closeConWLogging():
	closeFCW()
	return "success"
	
def openFC():
	fileC = open(confile, 'a')
def closeFC():
	fileC.close()

def openFCW():
	fileC = open(conwfile, 'a')
def closeFCW():
	fileC.close()
	
def write(logList):
	logfile = open(filename, 'a')
	for entry in logList:
		logfile.write(entry)
	del logList[:]
	logfile.close()

def writeCon(openFile, data):
	logfile = open(openFile, 'a')
	#logfile = openFile
	#logfile.write(data)
	for entry in data:
		logfile.write(entry)
	del data[:]
	logfile.close()
	

if __name__ == '__main__':
    app.run(port=8080, debug=True)
