from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import logging

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def incoming_sms():
	body = request.values.get('Body', None)
	str(body)
	resp = MessagingResponse()
	logging.debug(body)
	resp.message("Hello world!")
	return str(resp)

logging.basicConfig(level=logging.DEBUG, filename='log', filemode='a+', format='%(asctime)s %(message)s')

if __name__ == "__main__":
	app.run(debug=True, port = int(os.environ.get('PORT')))
