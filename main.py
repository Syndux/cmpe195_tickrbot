# Run command in shell when starting project, python3 -m pip install -U discord.py

import discord
from discord.ext import commands
from tabulate import tabulate
import os
import yfinance as yf


# bot = discord.ext.commands.Bot(command_prefix = "!");

client = discord.Client()

amc = yf.Ticker('AMC')
price = str(amc.info['currentPrice'])
sector = amc.info['sector']


# ------ Earliest Options Expiration ---------

op = amc.options
earlyExpiration = op[0]
opt = amc.option_chain(earlyExpiration)
calls = opt.calls.head()

# calls.type
# df = calls.DataFrame({'Date': [calls['contractSymbol']],'Strike':[calls['strike']]})

gme = yf.Ticker('GME')
gprice = str(gme.info['currentPrice'])
gsector = gme.info['sector']
gsumm = gme.info['longBusinessSummary']

op1 = gme.options
# earlyExpiration = op1[0]
opt1 = gme.option_chain(earlyExpiration)
calls1 = opt1.calls.head()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!AMC'):
    await message.channel.send('Current Price of AMC: $'+ price)
    await message.channel.send("Sector: " + sector)
    await message.channel.send("Call options: ")
    print(calls)
    await message.channel.send(calls)

    # await message.channel.send(tabulate(calls, headers='keys', tablefmt='psql'))


  if message.content.startswith('!GME'):
    await message.channel.send('`Current Price of GME: $'+ gprice +'`')
    await message.channel.send("`Sector: " + gsector +'`')
    await message.channel.send("Call options: ")
    await message.channel.send(calls1)
    await message.channel.send("`Summary: " + gsumm+'`')



#------------------- User Command Parsing ---------------------
# @commands.command()
# async def test(ctx, arg):
#     await ctx.send(arg)

# bot.add_command(test)

# @bot.command()
# async def test(bot, arg):
#     await bot.send(arg)



client.run(os.environ['TOKEN'])
# bot.run(os.environ['TOKEN'])

