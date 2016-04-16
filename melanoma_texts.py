import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
ACCOUNT_SID = "ACa9cf21438e147f669df6f794d7000122" 
AUTH_TOKEN = "5e3825edd333abc5fa4e094fba22c989"

app = Flask(__name__)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/", methods=['GET','POST'])
def reply():
	resp = twilio.twiml.Response()
	resp.message("Hello")
	print("got a message")
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug = True)