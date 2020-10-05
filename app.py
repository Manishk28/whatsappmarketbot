#TWILIO_ACCOUNT & TWILIO_TOKEN env variable where acc and token are stored.
from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os

app = Flask(__name__)

ACCOUNT_ID = os.environ.get("TWILIO_ACCOUNT")
TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = "whatsapp:+14155238886"
client = Client(ACCOUNT_ID,TOKEN)

def process_msg(msg):
    response = ""
    if msg == 'Hi':
        response = "Hello, Welcome to the stock market bot."
        response += "Please type code:<stock code> to know the price of the stock."
    elif 'code' in msg :
        data = msg.split(":")
        stock_code = data[1]
        stock_price =  get_stock_price(stock_code)
        last_price = stock_price['last_price']
        last_price = str(last_price)
        response = "The stock price of " + stock_code + " is $" + last_price
    else:
        response = "Please type \"Hi\" to get started."
    return response

def send_msg(msg, recipient):

    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

@app.route("/")
def hello():
    return {
        "Result" : "we have created first route"
    }

@app.route("/testpost", methods=["POST"])
def testpost():
    message = request.form["message"]
    return {
        "Result" : message
    }

@app.route("/webhook", methods=["POST"])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    #import pdb
    #pdb.set_trace()
    return "OK", 200
