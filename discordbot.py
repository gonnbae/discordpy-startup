from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command()
async def chimpo(ctx):
    await ctx.send('ちんちん')
    
@bot.command()
async def inu(ctx):
    await ctx.send('わんわん')
        
    
@bot.event  
async def on_member_join(member):  
    CHANNEL_ID = 694553669055807508 
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send('こんにちは、' +str(member.mention)+
                       'さん！よろしくお願いします！👍')

@bot.event    
    async def on_message(message):
if message.content.startswith('対戦募集')
    await message.channel.send(<@&701098449864622091> + message.author.name + 'さんが対戦募集しています！')



bot.run(token)
