from fastapi import FastAPI
from scrapper import get_dollar_rate


app = FastAPI()
baseUrl = '/api/v1'


@app.get(baseUrl + '/dollarRate')
async def getRate() -> dict:
  buy_rate, sell_rate = await get_dollar_rate()
  return {'buy_rate': buy_rate, 'sell_rate': sell_rate}

