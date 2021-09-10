from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import *
import smtplib
from pycoingecko import CoinGeckoAPI


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'krypto'
api = Api(app)
cg = CoinGeckoAPI()

jwt = JWT(app, authenticate, identity)

sender='dummy@gmail.com'
senderpass ='dummy121'


def send(price, recieversemail):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, senderpass)

    message = "Your Alert for Bitcoin has been triggered. \n Current Price of Bitcoin = {}".format(price['price'])

    server.sendmail(sender, recieversemail, message)

    server.quit()


api.add_resource(Alert, '/alerts/create/<int:price>')

if __name__ == '__main__':
    app.run(debug=True)
