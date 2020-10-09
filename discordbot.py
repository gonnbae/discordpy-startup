from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)




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
async def on_message(message):
    if message.content.startswith('対戦募集'):
        await message.channel.send(f'<@&701098449864622091>{message.author.name}さんが対戦募集していますん')
    await bot.process_commands(message)
    
    if message.content.startswith('たいぼ'):
        await message.channel.send(f'<@&701098449864622091>{message.author.name}さんがたいぼしていますん')
    await bot.process_commands(message)



    
bot.run(token)
