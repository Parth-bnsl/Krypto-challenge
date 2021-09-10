from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import smtplib

from pycoingecko import CoinGeckoAPI

sender='dummy@gmail.com'
senderpass ='dummy121'

c = CoinGeckoAPI()
def send(price, recieversemail):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, senderpass)

    message = "Your Alert for Bitcoin has been triggered. \n Current Price of Bitcoin = {}".format(price['price'])

    server.sendmail(sender, recieversemail, message)

    server.quit()

class Alert(Resource):
    TABLE_NAME = 'users'
    def __init__(self, username):
        self.username = username
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    @jwt_required()
    def post(self,username):
        receiversemail = username
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT price FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()






