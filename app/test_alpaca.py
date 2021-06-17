from alpaca_trade_api.rest import REST, TimeFrame, URL
import json
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

with open("config.json","rb") as file:
    config = json.load(file)

api = REST(key_id=config['alpaca_key_id'],
           secret_key=config['alpaca_secret_key'],
           base_url=URL(config['alpaca_base_url'])
           )

result = api.get_bars("AAPL", TimeFrame.Hour, "2021-02-08", "2021-02-08", limit=10, adjustment='raw').df

print(type(result))
print(result)
