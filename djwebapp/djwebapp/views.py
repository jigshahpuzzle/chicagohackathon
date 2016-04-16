from django.http import HttpResponse
 
def sms(request):
  twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
  return HttpResponse(twiml, content_type='text/xml')
  
