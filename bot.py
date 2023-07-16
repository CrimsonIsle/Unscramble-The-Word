import discord
import random
import time
import asyncio
import requests

from Website import URL
from discord.ext import commands
from yourtoken import BOT_TOKEN # Get token from file

intents = discord.Intents.default()
intents.message_content = True

response = requests.get(URL)
words = [line.strip() for line in response.text.split('\n') if len(line.strip()) > 2]

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def scramble(ctx):
    # Choose a random word from the list
    word = random.choice(words)

    # Generate an anagram of the word
    scramble = ''.join(random.sample(word, len(word)))

    # Send the anagram to the channel and count how long it took
    start_time = time.time()
    await ctx.send(f'Your word is: {scramble}')

    # Check if the message content is the same as given word
    def check(msg):
        return msg.content.lower() == word.lower()

    try:
        msg = await bot.wait_for('message', check=check, timeout=40.0)  # Time for solving

        end_time = time.time()  # Calculate the elapsed time and congratulate the user
        elapsed_time = round(end_time - start_time, 2)

        if msg.author == ctx.author:
            await ctx.send(f'Congratulations, {msg.author.mention}! You unscrambled the word in {elapsed_time} seconds!')
        else:
            await ctx.send(
                f'Congratulations, {msg.author.mention}! You unscrambled {ctx.author.mention}\'s word in {elapsed_time} seconds!')

    except asyncio.TimeoutError:
        await ctx.send(f"Sorry, {ctx.author.mention}, you ran out of time! The word was {word}!")



bot.run(BOT_TOKEN)