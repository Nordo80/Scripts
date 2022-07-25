from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os, time

app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms_bot():
    resp = MessagingResponse()
    incoming_msg = request.values.get('Body', '').lower()
    if "service apache2 start" in incoming_msg:
        service_start = os.system("echo 221298 | sudo -S -k service apache2 start")
        apache2 = os.system('systemctl is-active --quiet apache2')
        if apache2 == 0:
            msg = resp.message("Apache server is UP now!")
        else:
            msg = resp.message("Error! Apache problem!")
    else:
        msg = resp.message("Command not found.")
    return str(resp)
app.run()
