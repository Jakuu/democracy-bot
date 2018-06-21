//democracy-bot.py

client = discord.Client()

@client.event
async def on_ready():
    print('Democracy Online')


client.run(TOKEN)
