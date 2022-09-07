# Dollar Rate API 📈
A FASTAPI that returns the current ```unofficial``` dollar rate from the black market.
It uses [FASTAPI](https://fastapi.tiangolo.com/) server hosted on [render](https://render.com).

<br>
<br>
<br>
<br>

# How to use 🔍️
Send a ```GET``` request to the following URL to get the current dollar rate:



<a href="https://rate.onrender.com/api/v1/dollarRate">
https://rate.onrender.com/api/v1/dollarRate
</a>

<br>
The format of the response is JSON, as follows:

```
{
    "buy_rate":"number",
    "sell_rate":"number"
}
```

Currently their is only one endpoint ```/api/v1/dollarRate```, but there will be more in the future, for sayrfa rate and other currencies.

<br>
<br>
<br>
<br>

# How it works ✨
The API uses a web scraper ```BeautifulSoup``` to get the current dollar rate from the black market. The scrapper runs on every request, it scrapes the data from: ```https://lbprate.com/``` and returns the data, then the API returns the scraped data.
<br>
<br>
<br>
<br>
# How to run 🚀

For the Packages:
``` 
pip install -r requirements.txt
```
To run the server:
```
uvicorn main:app
```

<br>
<br>
<br>
<br>

# Contributing 💡
For any issues or suggestions, please open an issue on this Github repository. Contributors are welcome!
# License 📄
This project is licensed under the MIT license. See the LICENSE file for more information.