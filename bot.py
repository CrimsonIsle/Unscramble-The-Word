import discord
import random
import time
import asyncio

from discord.ext import commands
from yourtoken import BOT_TOKEN #get token from file

intents = discord.Intents.default() 
intents.message_content = True

with open('words.txt', 'r') as f:
    words = [line.strip() for line in f]

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
    
    # Wait for a message from the user
    def check(msg):
        return msg.author == ctx.author and msg.content.lower() == word.lower()
        
    try:
        msg = await bot.wait_for('message', check=check, timeout=35.0) #how much time for solving
    except asyncio.TimeoutError:
        await ctx.send(f"Sorry, {ctx.author.mention}, you ran out of time! The word was {word}!")
    
    else:
        end_time = time.time() # Calculate the elapsed time and congratulate the user
        elapsed_time = round(end_time - start_time, 2)
        await ctx.send(f'Congratulations, {ctx.author.mention}! You guessed the word in {elapsed_time} seconds!')
        
bot.run(BOT_TOKEN)

#To run type: python bot.py