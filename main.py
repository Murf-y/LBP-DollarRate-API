from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scrapper import get_dollar_rate


app = FastAPI()
baseUrl = '/api/v1'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(baseUrl + '/dollarRate')
async def getRate() -> dict:
  buy_rate, sell_rate = await get_dollar_rate()
  return {
    'buy_rate': buy_rate,
    'sell_rate': sell_rate
  }
