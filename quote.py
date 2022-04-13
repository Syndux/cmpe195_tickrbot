import os
import finnhub
import discord

API_KEY = os.environ['finnhub']
finnhub_client = finnhub.Client(api_key=os.environ['finnhub'])

not_found = discord.Embed(
    color = discord.Color.red(),
    title = "Stock symbol does not exist.",
    description = "!help quote for more info."
)

def get_quote(symbol):
    stock_quote = finnhub_client.quote(symbol={symbol.upper()})
    stock_name = finnhub_client.company_profile2(symbol={symbol.upper()})
    print(stock_name)
    name = stock_name['name']
    if stock_quote['c'] == 0:
        print(stock_quote['c'])
        return not_found
    elif (not stock_name): # needs to check if stock_name returns empty or has value
        print("test")
        return not_found
    else:
        if stock_quote['d'] > 0:
            change_color = discord.Color.green()
        elif stock_quote['d'] < 0:
            change_color = discord.Color.red()
        else:
            change_color = discord.Color.light_grey()

    embed = discord.Embed(
        color = change_color,
        title = f'{symbol.upper()} - {name} - Information Today' 
    )
    
    embed.add_field(name = 'Current Price: ', value = f"{round(stock_quote['c'], 2)}", inline = False)
    embed.add_field(name = 'Open: ', value = f"{round(stock_quote['o'], 2)}", inline = False)
    embed.add_field(name = 'Today\'s High: ', value = f"{round(stock_quote['h'], 2)}", inline = False)
    embed.add_field(name = 'Today\'s Low: ', value = f"{round(stock_quote['l'], 2)}", inline = False)
    
    return embed