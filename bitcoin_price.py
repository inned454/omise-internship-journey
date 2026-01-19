import requset

def get_bitcoin_price():
    # เราจะดึงข้อมูลราคา Bitcoin จาก Public API
    url = "https://api.bitkub.com/api/market/ticker?sym=THB_BTC"
    response = requests.get(url)

    if respones.status_code == 200:
        data = response.json()
        bitcoin_price = data['THB_BTC']['last']
        return bitcoin_price
    else:
        print("Error fetching data from API")
        
if __name__ == "__main__":
    get_bitcoin_price()