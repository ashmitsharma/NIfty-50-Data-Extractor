from bs4 import BeautifulSoup
import pandas as pd
import requests

names=[]
opens=[]
highs=[]
lows=[]
closes=[]

r = requests.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("table", {"class": "tbldata14 bdrtpg"})
links = results.findAll("td", {"class": "brdrgtgry"})
#links = results.findAll("a", {"class": "bl_12"})
#print(links)
for items in links:
    try:
        item_href = items.find("a").attrs["href"]
        if "optex" in item_href:
            list.remove(item_href)
        url = "https://www.moneycontrol.com"+item_href
        s = requests.get(url)
        soup = BeautifulSoup(s.text, "html.parser")
        resultss = soup.find("div", {"id": "mc_mainWrapper"})
        nametag = resultss.find("div", {"id": "stockName"})
        name = nametag.find("h1").text
        close = resultss.find("div", {"id": "nsecp"}).text
        low = resultss.find("div", {"id": "sp_low"}).text
        high = resultss.find("div", {"id": "sp_high"}).text
        open = resultss.find("td", {"class": "nseopn bseopn"}).text
        names.append(name)
        opens.append(open)
        highs.append(high)
        lows.append(low)
        closes.append(close)
        print('.',end = '')

    except:
        pass

df = pd.DataFrame({'Name':names,'Open':opens,'High':highs, 'Low':lows, 'Close':closes})
df.to_csv('stockdata.csv', index=False, encoding='utf-8')
print('')
print("Data Extracted Successfully")