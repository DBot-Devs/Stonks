from msilib.schema import Error
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import pandas_datareader as pdr
import requests

def GetStocks(Ticker):        
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":str(Ticker),"datatype":"json","output_size":"compact"}

    headers = {
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
        "X-RapidAPI-Key": "d9530def8dmsh6dcb6776fae04afp146fe2jsn3cf4b9769aba"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return response.text

bot = commands.Bot(command_prefix='$')

intents = discord.Intents.default()
intents.members = True

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():    
    print("bot ready")
    
@client.event
async def on_message(message):
    if (message.author == client.user):
        return
        
    if message.content.startswith("$ticker"):                        
        tempvar = GetStocks(message.content[8:12])
        await message.reply(  str(tempvar)[:2000]  )

client.run(TOKEN)   