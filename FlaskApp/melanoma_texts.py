import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, send_from_directory
from subprocess import check_output
import subprocess
from flask import render_template
import os
from shutil import copyfileobj
import requests
import send_sms
from imp import load_source
clean = load_source("resize_pics",os.path.abspath('..') + "/pyconv/images/resize_pics.py")
cnn = load_source("predict", os.path.abspath('..') + "/pyconv/predict.py")

ACCOUNT_SID = "ACa9cf21438e147f669df6f794d7000122" 
AUTH_TOKEN = "5e3825edd333abc5fa4e094fba22c989"
#th convnet.lua --cp cp_name --img img_name evalPic
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
		print(url)
		if mediatype[6:] == 'jpeg':
			extension = '.jpeg'
		elif mediatype[6:] == 'png':
			extension = '.png'
		path = os.path.realpath('../pyconv/images/') + "/" + str(number) + extension
		print(path)
		resp = twilio.twiml.Response()
		try:
			image = requests.get(url, stream = True)
			if image.status_code == 200:
				with open(path, 'wb') as f:
					image.raw.decode_content = True
					copyfileobj(image.raw, f)
			#sp = subprocess.Popen([os.path.abspath(os.curdir) + "/./conv"])
			clean.resizeToSquare(path, os.path.abspath('..') + "/pyconv/images/" + str(number) + extension)
			####result = check_output(['lua','-l','dummy', '-e', 'evalPic("%s")' %(path)], cwd = os.path.abspath('..') + "/pyconv")
			result = cnn.predict(os.path.abspath(os.curdir) + "/net.pkl", os.path.abspath(os.curdir) + "/images/image.pkl")
			send_sms.sendMessage(result, "+" + number)
			return str(resp)
		except IOError:
			resp.message("An error occured when processing your image. Please try again")
			return str(resp)


@app.route("/", methods=['GET', 'POST']) 
def home(): 
  return render_template("main.html")
	
if __name__ == "__main__":
	app.run(debug = True)
