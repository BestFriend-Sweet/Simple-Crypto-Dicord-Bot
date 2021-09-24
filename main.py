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
doge_data = cg.get_price(ids='dogecoin', vs_currencies='gbp')


def get_more_data(coin):
    more_data = cg.get_coins_markets(vs_currency="gbp", ids=f"{coin}")
    coin_name = more_data[0]["name"]
    coin_market_cap = more_data[0]["market_cap"]
    coin_high_24h = more_data[0]["high_24h"]
    coin_low_24h = more_data[0]["low_24h"]
    coin_price_change_percent = more_data[0]["price_change_percentage_24h"]
    coin_circulating_supply = more_data[0]["circulating_supply"]
    coin_ath_price = more_data[0]["ath"]
    coin_ath_change_percent = more_data[0]["ath_change_percentage"]
    coin_image = more_data[0]["image"]
    coin_current_price = more_data[0]["current_price"]
    coin_atl = more_data[0]["atl"]

    return coin_name, coin_market_cap, coin_high_24h, coin_low_24h, coin_price_change_percent, coin_circulating_supply, coin_ath_price, coin_ath_change_percent, coin_image, coin_current_price, coin_atl



[btc_coin_name, 
    btc_coin_market_cap, 
    btc_coin_high_24h, 
    btc_coin_low_24h, 
    btc_coin_price_change_percent, 
    btc_coin_circulating_supply, 
    btc_coin_ath_price, 
    btc_coin_ath_change_percent, 
    btc_coin_image, 
    btc_coin_current_price, 
    btc_coin_atl] = get_more_data("bitcoin")

[xrp_coin_name, 
    xrp_coin_market_cap, 
    xrp_coin_high_24h, 
    xrp_coin_low_24h, 
    xrp_coin_price_change_percent, 
    xrp_coin_circulating_supply, 
    xrp_coin_ath_price, 
    xrp_coin_ath_change_percent, 
    xrp_coin_image, 
    xrp_coin_current_price, 
    xrp_coin_atl] = get_more_data("ripple")

[eth_coin_name, 
    eth_coin_market_cap, 
    eth_coin_high_24h, 
    eth_coin_low_24h, 
    eth_coin_price_change_percent, 
    eth_coin_circulating_supply, 
    eth_coin_ath_price, 
    eth_coin_ath_change_percent, 
    eth_coin_image, 
    eth_coin_current_price, 
    eth_coin_atl] = get_more_data("ethereum")

[link_coin_name, 
    link_coin_market_cap, 
    link_coin_high_24h, 
    link_coin_low_24h, 
    link_coin_price_change_percent, 
    link_coin_circulating_supply, 
    link_coin_ath_price, 
    link_coin_ath_change_percent, 
    link_coin_image, 
    link_coin_current_price, 
    link_coin_atl] = get_more_data("chainlink")

[ada_coin_name, 
    ada_coin_market_cap, 
    ada_coin_high_24h, 
    ada_coin_low_24h, 
    ada_coin_price_change_percent, 
    ada_coin_circulating_supply, 
    ada_coin_ath_price, 
    ada_coin_ath_change_percent, 
    ada_coin_image, 
    ada_coin_current_price, 
    ada_coin_atl] = get_more_data("cardano")


[avax_coin_name, 
    avax_coin_market_cap, 
    avax_coin_high_24h, 
    avax_coin_low_24h, 
    avax_coin_price_change_percent, 
    avax_coin_circulating_supply, 
    avax_coin_ath_price, 
    avax_coin_ath_change_percent, 
    avax_coin_image, 
    avax_coin_current_price, 
    avax_coin_atl] = get_more_data("avalanche-2")

[doge_coin_name, 
    doge_coin_market_cap, 
    doge_coin_high_24h, 
    doge_coin_low_24h, 
    doge_coin_price_change_percent, 
    doge_coin_circulating_supply, 
    doge_coin_ath_price, 
    doge_coin_ath_change_percent, 
    doge_coin_image, 
    doge_coin_current_price, 
    doge_coin_atl] = get_more_data("dogecoin")

[vet_coin_name, 
    vet_coin_market_cap, 
    vet_coin_high_24h, 
    vet_coin_low_24h, 
    vet_coin_price_change_percent, 
    vet_coin_circulating_supply, 
    vet_coin_ath_price, 
    vet_coin_ath_change_percent, 
    vet_coin_image, 
    vet_coin_current_price, 
    vet_coin_atl] = get_more_data("vechain")


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
        The following crypto prices are available, btc, eth, xrp, link, vet, dogecoin, ada, and avax.
        To get the price of your chosen coin/token, simply place '$' before the abbreviated name of your token. For example $eth
        List of available commands:
        $trending""")

    if message.content.startswith("$trending"):
        await message.channel.send(f"Top 7 trending search coins\n-------------------------------------\n{trending_coins}")

    if message.content.startswith("$market_dominance"):
        await message.channel.send(f"Market Cap Percentage\n-------------------------------------\n{market_dom}")
        
    if message.content.startswith("$about"):
        await message.channel.send(f"Thank you for using this discord bot.\nTo view how I was made visit here: {repository}")


    if message.content.startswith('$btc'):
        
        #### Create the initial embed object ####
        embed=discord.Embed(title=f"{btc_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{btc_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(btc_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(btc_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(btc_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(btc_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(btc_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(btc_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(btc_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(btc_coin_ath_change_percent), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(btc_coin_atl), inline=True)

        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")

        await message.channel.send(embed=embed)

    if message.content.startswith('$xrp'):
        
        #### Create the initial embed object ####
        embed=discord.Embed(title=f"{xrp_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{xrp_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(xrp_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(xrp_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(xrp_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(xrp_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(xrp_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(xrp_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(xrp_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(xrp_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(xrp_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)

    if message.content.startswith('$eth'):
        
        #### Create the initial embed object #eth
        embed=discord.Embed(title=f"{eth_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{eth_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(eth_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(eth_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(eth_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(eth_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(eth_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(eth_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(eth_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(eth_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(eth_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)
    
    if message.content.startswith('$link'):
        
        #### Create the initial embed object #eth
        embed=discord.Embed(title=f"{link_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{link_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(link_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(link_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(link_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(link_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(link_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(link_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(link_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(link_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(link_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)
    
    if message.content.startswith('$ada'):
        
        #### Create the initial embed object #eth
        embed=discord.Embed(title=f"{ada_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{ada_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(ada_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(ada_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(ada_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(ada_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(ada_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(ada_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(ada_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(ada_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(ada_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)

    if message.content.startswith('$avax'):
        
        #### Create the initial embed object #eth
        embed=discord.Embed(title=f"{avax_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{avax_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(avax_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(avax_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(avax_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(avax_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(avax_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(avax_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(avax_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(avax_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(avax_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)

    if message.content.startswith('$doge'):
        
        #### Create the initial embed object #eth
        embed=discord.Embed(title=f"{doge_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{doge_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(doge_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(doge_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(doge_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(doge_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(doge_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(doge_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(doge_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(doge_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(doge_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)
    
    if message.content.startswith('$vet'):
        
        #### Create the initial embed object #eth
        embed=discord.Embed(title=f"{vet_coin_name}")

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar_url)

        embed.set_thumbnail(url=f"{vet_coin_image}")

        embed.add_field(name="Current Price 💵", value="£{:,}".format(vet_coin_current_price), inline=True)
        embed.add_field(name="Circulating Supply 🪙", value="{:,}".format(vet_coin_circulating_supply), inline=True)
        embed.add_field(name="Market Cap 🤑", value="£{:,}".format(vet_coin_market_cap), inline=True)

        embed.add_field(name="24h-High ⬆️", value="£{:,}".format(vet_coin_high_24h), inline=True)
        embed.add_field(name="24h-low ⬇️", value="£{:,}".format(vet_coin_low_24h), inline=True)
        embed.add_field(name="Price Change 24h ⏰", value="{:,}%".format(round(vet_coin_price_change_percent, 2)), inline=True)

        embed.add_field(name="All Time High 👑", value="£{:,}".format(vet_coin_ath_price), inline=True)
        embed.add_field(name="ATH Percent Change 📊", value="{:,}%".format(round(vet_coin_ath_change_percent, 2)), inline=True)
        embed.add_field(name="ATL 😢", value = "£{:,}".format(vet_coin_atl), inline=True)


        embed.set_footer(text="Thank you for using Crypto Bot Price Checker 🙏")


        await message.channel.send(embed=embed)


client.run("{replace with your own token}")
