import aiohttp
from bs4 import BeautifulSoup
async def get_info_from(url):
    # Get the page, add header to avoid 403 error, await the request

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            html = await response.text()
        
    # Parse the page
    soup = BeautifulSoup(html, 'html.parser')
    # Get the information
    info = soup.find_all(class_='col-md-4')
    # Get the data
    data = []
    for i in info:
        data.append(i.get_text())
    # Return the data
    return data

async def get_dollar_rate():
    # Get the url
    url = 'https://lbprate.com/'
    # Get the data using event loop
    data = await get_info_from(url)
    buy_rate = data[0].split('\n')[3].split(' ')[4]
    sell_rate =data[1].split('\n')[3].split(' ')[4]
    # Print the data
    return buy_rate, sell_rate