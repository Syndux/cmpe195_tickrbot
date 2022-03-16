import discord
import requests
import os


def get_chart(symbol, duration):
    temp_duration = 'i5'
    duration_options = ['M','m','W','w','D','d','15','5','3']
    if(duration == 'M' or duration == 'm'):
        temp_duration = 'M'
    elif(duration == 'W' or duration == 'w'):
        temp_duration = 'W'
    elif(duration == 'D' or duration == 'd'):
        temp_duration = 'D'
    elif(duration == '15'):
        temp_duration = 'i15'
    elif(duration == '5'):
        temp_duration = 'i5'
    elif(duration == '3'):
        temp_duration = 'i3'          

    daily_indicators = 'rsi_b_14,macd_b_12_26_9,ema_9,ema_21,sma_50,sma_200,sma_20'
    indicators = daily_indicators if (duration == 'd' or duration == 'D') else '0'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    
    url = f'https://elite.finviz.com/chart.ashx?t={symbol}&ty=c&ta={indicators}&p={temp_duration}&s=l'

    if (duration not in duration_options):
        return 'Incorrect time period.'
    else:
        response = requests.get(url, headers=headers)
        if not os.path.exists('charts'):
            os.mkdir('charts')
    
        with open(os.path.join('charts', f'chart_{symbol}{duration}.png'), 'wb') as handle:
            handle.write(response.content)
        
        return True
        