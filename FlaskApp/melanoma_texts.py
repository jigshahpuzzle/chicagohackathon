import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, send_from_directory
from subprocess import check_output
from flask import render_template
ACCOUNT_SID = "ACa9cf21438e147f669df6f794d7000122" 
AUTH_TOKEN = "5e3825edd333abc5fa4e094fba22c989"

#convnet.lua
#.t7
app = Flask(__name__)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/sms", methods=['GET','POST'])
def reply():
	number = request.values.get('From', None)[1:]
	nmedia = request.values.get('NumMedia', None)
	mediatype = request.values.get('MediaContentType0',None)
	if (nmedia > 0) & (mediatype[0:5] == 'image'):
		url = request.values.get('MediaUrl0', None)
		if mediatype[6:] == 'jpeg':
			extension = '.jpeg'
		elif mediatype[6:] == 'png':
			extension = '.png'
		path = os.path.realpath('../conv/')
		resp = twilio.twiml.Response()
		try:
			urlretrieve(url, path + str(number) + extension)
			resp.message("Your image has been received and is being analyzed. You will receive a response shortly.")
			return str(resp)
		except IOError:
			resp.message("An error occured when processing your image. Please try again")
			return str(resp)


@app.route("/", methods=['GET', 'POST']) 
def home(): 
  return render_template("main.html")
	
if __name__ == "__main__":
	app.run(debug = True)
