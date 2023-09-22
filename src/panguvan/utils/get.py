import httpx
import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


def get(url, timeout=(1, 3)):
    return httpx.get(url, headers=headers, timeout=timeout)


def get_last_market_activity_datetime():
    url = "http://cdn.tsetmc.com/api/MarketData/GetMarketOverview/1"
    main = get(url).json().get("marketOverview")
    date = main.get("marketActivityDEven")
    time = main.get("marketActivityHEven")
    return datetime.datetime.strptime(f"{date} {time}", "%Y%m%d %H%M%S")
