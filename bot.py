import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "jak nie bez powodu nazywaja jb?":
        await message.channel.send("obsraniec")

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "chuj":
        await message.channel.send("ci w dupe")

    await bot.process_commands(message)

@bot.command()
async def testgigga(ctx):
    await ctx.send(f'hello my nigga {ctx.author}')

@bot.command()
async def calc(ctx, *, expression: str):
    try:
        # Pozwalamy tylko na cyfry i podstawowe operatory
        allowed = "0123456789+-*/(). "
        if not all(char in allowed for char in expression):
            await ctx.send("Dozwolone są tylko cyfry i operatory + - * / ( )")
            return
        result = eval(expression)
        await ctx.send(f"Wynik: {result}")
        
    except Exception as e:
        await ctx.send("Błąd w wyrażeniu.")

bot.run(TOKEN)
