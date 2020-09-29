# bot.py
import os
import random
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='glados', help='Dispenses GLaDOS quotes')
async def glados(ctx):
	glados_quotes = open(Path.cwd() / 'glados_quotes_file.txt') 

	response = random.choice(glados_quotes.readlines())
	await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
