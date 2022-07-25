import os, time
from twilio.rest import Client
import netifaces

account_sid = 'ACd029985a506b097e15ec17e013f7e615'
auth_token = '71dd5ab2cfcedc72cefafe4d0dac68d3'

def status_check():
    while True:
        apache2 = os.system('systemctl is-active --quiet apache2')
        ip = netifaces.ifaddresses('virbr0')[netifaces.AF_INET][0]['addr']
        if apache2 == 0:
            print('Its okay')
        else:
            client = Client(account_sid, auth_token)
            client.api.account.messages.create(
                to="+37253754954",
                from_="+15088120994",
                body=f"The Web Server {ip} is Down!")
            print("ploho")
        time.sleep(30)
status_check()



