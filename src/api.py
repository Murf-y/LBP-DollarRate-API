from gevent import monkey
from gevent.pywsgi import WSGIServer

from flask import Flask , jsonify
from scrapper import get_dollar_rate


monkey.patch_all()
app = Flask(__name__)

api = "/api/v1/"

@app.route(api + "dollarRate")
async def getRate():
  buy_rate, sell_rate = await get_dollar_rate()
  return jsonify({'buy_rate': buy_rate, 'sell_rate': sell_rate})


if __name__ == '__main__':
    # Create WSGI server with params for Repl.it (IP 0.0.0.0, port 8080)
    # for our Flask app
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    # Start WSGI server
    http_server.serve_forever()