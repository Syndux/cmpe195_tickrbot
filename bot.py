import os
import discord
from discord.ext import commands
import chart as c
import quote as q

import random

description = 'TickrBot - A Python Discord Bot made by Group #24 of Sp\'22'
bot = commands.Bot(command_prefix='!', description = description)
bot.remove_command('help') # Help command

# Shows Discord bot online in console
@bot.event
async def on_ready():
    activity = discord.Game(name="!help for commands", type = 3)
    await bot.change_presence(status = discord.Status.online, activity=activity)
    print(f'{bot.user.name} logged in.')

# Shows Discord bot offline in console
@bot.event
async def on_disconnect():
    print(f'{bot.user.name} disconnected')

# Some error handling
@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(
        color = discord.Color.red()
    )
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(
            name = 'Missing an argument!',
            value = 'See !help for help.'
        )
        await ctx.send(embed = embed)

# !help <command> function
@bot.command(name = 'help')
async def help_command(ctx, command=None):
    author = ctx.message.author

    if command != None:
        embed = discord.Embed(
            color = discord.Color.blue(),
            title = 'TickrBot Help'
    )

    # Add !help commands here - alphabetize please
        if command == 'chart':
            embed.add_field(
                name = '!chart <symbol> <duration>',
                value = 'Generate a chart for given symbol in given duration. Durations: M, W, D, 15, 5, 3 are for the monthly, weekly, daily, 15, 5, and 3 minute.'
            )
    
        elif command == 'help':
            embed.add_field(
                name = 'Help Command',
                value = 'Help with the help?'
            )
        
        elif command == 'quote':
            embed.add_field(
                name = '!quote <symbol>',
                value = 'Get information about a specific stock.'
            )
        
        else:
            embed.add_field(
                name = 'Unknown Command',
                value = 'Command not recognized.'
            )

        await ctx.send(embed = embed)


    # List basic help info
    elif command == None:
        embed = discord.Embed(
            color = discord.Color.blue(),
            title = 'TickrBot Help \n!help <command> for help on a specific command.'
        )
        embed.add_field(
            name = '!chart <symbol> <duration>',
            value = 'Gets a stock chart in a specified duration.',
            inline = False
        )
        embed.add_field(
            name = '!help <command>',
            value = 'Get help with !help <command>.',
            inline = False
        )
        embed.add_field(
            name = '!quote <symbol>',
            value = 'Gets daily information on the specific symbol.',
            inline = False
        )
        embed.set_footer(
            text = 'TickrBot by Group #24 of SJSU - Sp\'22.\nDo your own due diligence if you choose to follow any information given by TickrBot. Any action is of your own accord. Group #24 and its affiliates are not liable for any losses you may incur.'            
        )

        await ctx.send(embed = embed)

# !chart <symbol> <duration> function
@bot.command(name = 'chart')
async def charting(ctx, symbol, duration):
    message = c.get_chart(symbol, duration)
    if message != True:
        await ctx.send(embed = message)
    else:
        filename = f'chart_{symbol}{duration}.png'
        with open(f'charts/chart_{symbol}{duration}.png', 'rb') as handle:
            image_send = discord.File(handle, filename = filename)
        await ctx.send(file = image_send)
        os.remove(f'charts/{filename}')
        
# !quote <symbol>        
@bot.command(name = 'quote')
async def quoting(ctx, symbol):
    embed = q.get_quote(symbol)
    await ctx.send(embed = embed)


#================================== FUN STUFF =======================================================================
@bot.command('sheesh')
async def sheesh(ctx):
    desc = ['(っ・ω・）っ≡≡≡≡≡≡.*･☆', '[^._.^]ﾉ', '( ˘•ω• ˘ )','(´⊙ω⊙` )ᵒᵐᵍᵎᵎᵎ', '┗(･ω･; )┛', '@(´ ･ｪ･ `)@']
    desc = random.choice(desc)
    embed=discord.Embed(
        title="SHEEeeeeEEESH!!!!!",
        description= desc,
        color= discord.Color.random())
    await ctx.send(embed=embed)


@bot.command('hot')
async def hot(ctx):
    desc = ['heads', 'tails']
    desc = random.choice(desc)
    embed=discord.Embed(
        title=desc,
        color= discord.Color.greyple())
    await ctx.send(embed=embed)

bot.run(os.environ['h_token'])