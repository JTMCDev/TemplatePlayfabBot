# template made by jtmc
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot, has_permissions, CheckFailure
import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

#Pretty much ignore this next line.
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all()) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.tree.sync() #sync the command tree

def make_playfab_request(path, payload=None, method='post'):
    url = f'https://{config["playfab_title_id"]}.playfabapi.com/{path}'
    headers = {
        'X-SecretKey': config["playfab_secret_key"],
        'Content-Type': 'application/json'
    }

    if method == 'post':
        response = requests.post(url, json=payload, headers=headers)
    elif method == 'get':
        response = requests.get(url, headers=headers)
    else:
        return None

    return response.json()






bot.run(config["discord_bot_token"])