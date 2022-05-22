# Dollar Rate API 📈
A Flask API that returns the current ```unofficial``` dollar rate from the black market.
It runs on a [Flask](https://flask.palletsprojects.com/en/1.1.x/) server hosted on [repl.it](https://repl.it/languages/python3).

<br>
<br>
<br>
<br>

# How to use 🔍️
Send a ```GET``` request to the following URL to get the current dollar rate:



```
https://dollarrateapi.murfyy.repl.co/api/v1/DollarRate
```
The format of the response is JSON, as follows:

```
{
    "buy_rate":"number",
    "sell_rate":"number"
}
```

Currently their is only one endpoint ```/api/v1/DollarRate```, but there will be more in the future, for sayrfa rate and other currencies.

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
To run the flask server:
```
python3 api.py
```

<br>
<br>
<br>
<br>

# Contributing 💡
For any issues or suggestions, please open an issue on this Github repository. Contributors are welcome!
# License 📄
This project is licensed under the MIT license. See the LICENSE file for more information.