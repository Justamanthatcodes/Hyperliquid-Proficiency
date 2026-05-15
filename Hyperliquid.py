from hyperliquid.info import Info
from hyperliquid.utils import constants

info = Info(constants.MAINNET_API_URL, skip_ws=True)

meta, contexts = info.meta_and_asset_ctxs()
universe = meta["universe"]
all_mids = info.all_mids()


for coin in universe:
    if coin["name"] == "BTC":
        print("Found!")
        
if "BTC" in all_mids:
    live_price = float(all_mids["BTC"])

print(f"Live price of bitcoin is ${live_price}")