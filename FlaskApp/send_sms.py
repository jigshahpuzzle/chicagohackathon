from twilio.rest import TwilioRestClient

def sendMessage(confidence_score, phone_number): 
	confidence_score = float(confidence_score)
	account_sid = "ACa9cf21438e147f669df6f794d7000122"
	auth_token = "5e3825edd333abc5fa4e094fba22c989"
	client = TwilioRestClient(account_sid, auth_token)
	if confidence_score > 0.9:
		message = client.messages.create(to=phone_number, from_="+14245439007",
	                                     body="Hello there! Our algorithms say that you have a %f chance of having skin cancer. We highly recommend you seek medical attention immediately." % (confidence_score))
	elif confidence_score > 0.5:
		message = client.messages.create(to=phone_number, from_="+14245439007",
	                                     body="Hello there! Our algorithms say that you have a %f chance of having skin cancer. It would be advisable to get it checked out!" % (confidence_score))
	else: 		
		message = client.messages.create(to=phone_number, from_="+14245439007",
	                                     body="Hello there! Our algorithms say that you have a %f chance of having skin cancer. You are probably okay!" % (confidence_score))
