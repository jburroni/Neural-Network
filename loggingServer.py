import json
import os, datetime
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

class logserver:
	

	firefile = ""
	confile = ""
	conwfile = ""
	
	def logFiring(self, log):
		self.writeLog(self.firefile, log)
		return "success"
	
	def logConnection(self, log):
		self.writeLog(self.confile, log)
		return "success"
	
	def logConW(self, log):
		self.writeLog(self.conwfile, log)
		return "success"
		
	def writeLog(self, filename, data):
		logfile = open(filename, 'a')
		for entry in data:
			logfile.write(entry)
		del data[:]
		logfile.close()

	def createNewLogFiles(self):
		logpath = os.path.dirname(os.getcwd())
		logpath = os.path.normpath(os.path.join(logpath, 'BrainPowerLogs'))
		conpath = os.path.normpath(os.path.join(logpath, 'Connections'))
		conwpath = os.path.normpath(os.path.join(logpath, 'ConWeights'))
		firepath = os.path.normpath(os.path.join(logpath, 'Firing'))
	
		timestampstr = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	
		self.firefile = os.path.join(firepath, timestampstr)
		self.confile  = os.path.join(conpath, timestampstr)
		self.conwfile = os.path.join(conwpath, timestampstr)

		lfile = open(self.firefile, 'w')
		lfile.close()
		lfile = open(self.confile, 'w')
		lfile.close()
		lfile = open(self.conwfile, 'w')
		lfile.close()
	
	def main(self):
		app.run(port=8080, debug=True)	

logserv = logserver()

@app.route("/")
def index():
	return render_template('index.html')
	
@app.route('/logging', methods=['POST'])
def log():
	log = request.get_json()
	logserv.logFiring(log)
	return "success"

@app.route('/connection', methods=['POST'])
def logConnections():
	log = request.get_json()
	logserv.logConnection(log)
	return "success"

@app.route('/conweights', methods=['POST'])
def logWeights():
	log = request.get_json()
	logserv.logConW(log)
	return "success"

@app.route('/createLogs', methods=['POST'])	
def createLogFiles():		
	logserv.createNewLogFiles()
	
if __name__ == '__main__':
    logserv.main()
    
