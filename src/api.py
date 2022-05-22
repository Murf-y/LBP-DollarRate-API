"""
FLASK API to request the current dollar rate from lbprate.com
it uses the scrapper.py to get the data
and then it returns the data in a json format
"""

from flask import Flask, jsonify
from src.scrapper import get_dollar_rate


app = Flask(__name__)
api = '/api/v1/'

# Get the dollar rate
@app.route(api + 'DollarRate', methods=['GET'])
async def get_rate():
    buy_rate, sell_rate = await get_dollar_rate()

    # Return the data
    return jsonify({'buy_rate': buy_rate, 'sell_rate': sell_rate})

# Run the app
if __name__ == '__main__':
    app.run()
    