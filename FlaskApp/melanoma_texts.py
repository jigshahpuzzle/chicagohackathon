import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
from subprocess import check_output
ACCOUNT_SID = "ACa9cf21438e147f669df6f794d7000122" 
AUTH_TOKEN = "5e3825edd333abc5fa4e094fba22c989"

#convnet.lua
#.t7
app = Flask(__name__)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/", methods=['GET','POST'])
def reply():
	number = request.values.get('From', None)
	print(number)
	resp = twilio.twiml.Response()
	print(resp)
	resp.message("Hello")
	print(request.values.get('NumMedia',None))
	print(request.form.get('media', ''))
	print(request.values.get('MediaUrl{0}',None))
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug = True)