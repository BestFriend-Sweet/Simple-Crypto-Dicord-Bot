from pycoingecko import CoinGeckoAPI
import discord
import os

cg = CoinGeckoAPI()

btc_data = cg.get_price(ids='bitcoin', vs_currencies='gbp')
eth_data = cg.get_price(ids='ethereum', vs_currencies='gbp')
xrp_data = cg.get_price(ids='ripple', vs_currencies='gbp') # People are still referring XRP as Ripple q-_-p
link_data = cg.get_price(ids='chainlink', vs_currencies='gbp')
avax_data = cg.get_price(ids='avalanche-2', vs_currencies='gbp')
vet_data = cg.get_price(ids='vechain', vs_currencies='gbp')



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

print(f"£{btc_price}")
print(f"£{eth_price}")
print(f"£{xrp_price}")
print(f"£{link_price}")
print(f"£{avax_price}")


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$help"):
        await message.channel.send("The following crypto prices are available, btc, eth, xrp, link, vet, and avax.\n To get the price of your chosen coin/token, simply place '$' before the abbreviated name of your token. For example $eth")

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
    



client.run("{replace with your own discord bot token}")
