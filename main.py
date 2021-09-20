from pycoingecko import CoinGeckoAPI
import discord
import os

cg = CoinGeckoAPI()

repository = "https://github.com/ColdBio/Simple-Crypto-Dicord-Bot"

btc_data = cg.get_price(ids='bitcoin', vs_currencies='gbp')
eth_data = cg.get_price(ids='ethereum', vs_currencies='gbp')
xrp_data = cg.get_price(ids='ripple', vs_currencies='gbp') # People are still referring XRP as Ripple q-_-p
link_data = cg.get_price(ids='chainlink', vs_currencies='gbp')
avax_data = cg.get_price(ids='avalanche-2', vs_currencies='gbp')
vet_data = cg.get_price(ids='vechain', vs_currencies='gbp')
ada_data = cg.get_price(ids='cardano', vs_currencies='gbp')
vet_data = cg.get_price(ids='vechain', vs_currencies='gbp')
doge_data = cg.get_price(ids='dogecoin', vs_currencies='gbp')

trending_data = cg.get_search_trending()
trending_tokens = []
count_1 = 1
for each in trending_data["coins"]:
    item = each["item"]["name"]
    trending_tokens.append(f"({count_1}). {item} \n")
    count_1 += 1

trending_coins = ''.join(trending_tokens)

market_percent_data = cg.get_global()
upcoming_ico_data = None
ongoing_ico_data = None
ended_ico_data = None

upcoming_ico_data = market_percent_data["upcoming_icos"]
ongoing_ico_data = market_percent_data["ongoing_icos"]
ended_ico_data = market_percent_data["ended_icos"]


market_cap_percentage_data = cg.get_search_trending()
market_cap_percentage = []
count_2 = 1
for k, v in market_percent_data["market_cap_percentage"].items():
    market_cap_percentage.append(f"({count_2}). {k}: {round(v, 2)}% \n")
    count_2 += 1
market_dom = ''.join(market_cap_percentage)

btc_key = list(btc_data.values())[0]
btc_price = list(btc_key.values())[0]

eth_key = list(eth_data.values())[0]
eth_price = list(eth_key.values())[0]

xrp_key = list(xrp_data.values())[0]
xrp_price = list(xrp_key.values())[0]

link_key = list(link_data.values())[0]
link_price = list(link_key.values())[0]

avax_key = list(avax_data.values())[0]
avax_price = list(avax_key.values())[0]

vet_key = list(vet_data.values())[0]
vet_price = list(vet_key.values())[0]

ada_key = list(ada_data.values())[0]
ada_price = list(ada_key.values())[0]

doge_key = list(doge_data.values())[0]
doge_price = list(doge_key.values())[0]


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$help"):
        await message.channel.send("""
        The following crypto prices are available, btc, eth, xrp, link, vet, and avax.
        To get the price of your chosen coin/token, simply place '$' before the abbreviated name of your token. For example $eth
        List of available commands:
        $trending""")

    if message.content.startswith("$trending"):
        await message.channel.send(f"Top 7 trending search coins\n-------------------------------------\n{trending_coins}")

    if message.content.startswith("$market_dominance"):
        await message.channel.send(f"Market Cap Percentage\n-------------------------------------\n{market_dom}")
        
    if message.content.startswith("$about"):
        await message.channel.send(f"Thank you for using this discord bot.\nTo view how I was made visit here: {repository}")

    if message.content.startswith("$btc"):
        await message.channel.send(f"£{btc_price}")
    
    if message.content.startswith("$eth"):
        await message.channel.send(f"£{eth_price}")
    
    if message.content.startswith("$xrp"):
        await message.channel.send(f"£{xrp_price}")
    
    if message.content.startswith("$link"):
        await message.channel.send(f"£{link_price}")
    
    if message.content.startswith("$avax"):
        await message.channel.send(f"£{avax_price}")
    
    if message.content.startswith("$vet"):
        await message.channel.send(f"£{vet_price}")
    
    if message.content.startswith("$ada"):
        await message.channel.send(f"£{ada_price}")
        
    if message.content.startswith("$doge"):
        await message.channel.send(f"£{doge_price}")
    

client.run("{replace with your own discord bot token}")
