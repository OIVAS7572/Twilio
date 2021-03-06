from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import logging
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def incoming_sms():
	body = request.values.get('Body', None)
	str(body)
	resp = MessagingResponse()
	print(body)
	logging.debug(body)
	resp.message("Hello world!")
	return str(resp)

logging.basicConfig(level=logging.DEBUG, filename='log', filemode='a+', format='%(asctime)s %(message)s')

port = int(os.environ['PORT'])

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=port)
