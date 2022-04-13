import os
import finnhub
import discord

finnhub_client = finnhub.Client(api_key=os.environ['finnhub'])

not_found = discord.Embed(
    color = discord.Color.red(),
    title = "Stock symbol does not exist.",
    description = "!help quote for more info."
)

def get_quote(symbol):    
    stock_quote = finnhub_client.quote(symbol={symbol.upper()})
    if stock_quote['c'] == 0:
        return not_found
    else:
        if stock_quote['d'] > 0:
            change_color = discord.Color.green()
        elif stock_quote['d'] < 0:
            change_color = discord.Color.red()
        else:
            change_color = discord.Color.light_grey()
    
    stock_name = finnhub_client.company_profile2(symbol={symbol.upper()})
    if stock_name == {}:
        name = symbol.upper()
    else:
        name = stock_name['name']
    
    embed = discord.Embed(
        color = change_color,
        title = f'{name} ({symbol.upper()}) Quote' 
    )
    
    embed.add_field(name = 'Current Price:', value = f"{round(stock_quote['c'], 2)}", inline = False)
    embed.add_field(name = 'Open:', value = f"{round(stock_quote['o'], 2)}", inline = False)
    embed.add_field(name = 'Today\'s Change:', value = f"{round(stock_quote['d'], 2)} ({round(stock_quote['dp'], 2)}%)", inline = False)
    embed.add_field(name = 'Today\'s High:', value = f"{round(stock_quote['h'], 2)}", inline = False)
    embed.add_field(name = 'Today\'s Low:', value = f"{round(stock_quote['l'], 2)}", inline = False)
    
    return embed