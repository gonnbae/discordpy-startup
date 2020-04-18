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
    
@bot.event  
async def on_member_join(member):  
    CHANNEL_ID = 694553669055807508 
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send('こんにちは、' +str(member.mention)+
                       'さん！よろしくお願いします！👍')
    



@bot.event
class AnnounceMatchMessageMaker(MessageMaker):
    def __init__(self):
        super(AnnounceMatchMessageMaker, self).__init__()
        MATCH_CHANNEL_ID =701111381633531905
　　　　STARVED_MATCHING =<@&701098449864622091>
        self.keyword = '対戦募集'
        self.output_replies = []
        self.message_pattern = 0
        self.ch_manager = ChannelManager()
        self.keychannel = self.ch_manager.MATCH_CHANNEL_ID
        print(type(self.keychannel))
        self.starved_matching = self.ch_manager.STARVED_MATCHING

    async def _makeMessage(self, message, client, channel=None) -> str:
        asyncio_result = None
        if self.message_pattern == -1:
            return asyncio_result
        if self.message_pattern == 0:
            self.reply = f'{message.author.mention} さんが対戦募集を開始しました。 {self.starved_matching}\n \
                参加したい方はこちらから→{message.channel.mention}  \n'
        self.output_replies.append(
            [client.get_channel(self.ch_manager.MATCH_CHANNEL_ID), self.reply])
        for reply_channel, reply_content in self.output_replies:
            asyncio_result = await reply_channel.send(reply_content)
        return asyncio_result

    async def executeFunction(self, message, client) -> str:
        asyncio_result = None
        # 「対戦募集」から始まってなかったら -1 パターンのメッセージを作成
        if not message.content.startswith(self.keyword):
            self.message_pattern = -1
            asyncio_result = await self._makeMessage(message, client)
            return asyncio_result
        # 対戦募集チャンネル「以外」でのメッセージはスルーする。
        if message.channel.id == self.keychannel:
            asyncio_result = await self._makeMessage(message, client)
        return asyncio_result

    def checkTriggers(self, message) -> bool:
        if self._checkKeyword(message) or self._checkChannelMessageWritten(message):
            return True
        return False

bot.run(token)
