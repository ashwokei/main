import discord, random, json, time, asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient

bot_name = "pyBot"
bot_prefix = "!"

with open("cord_token.json") as file_token:
    tok_data=json.load(file_token)              # gets token from json

client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all(), description="bot")
GUILD = []

emojiList = ['😭','😄','😌','🤓','😎','😤','🤖','😶‍🌫️','🌏','📸','💿','👋','🌊','✨','(stop spamming)']


def RandomEmoji():
    return random.choice(emojiList)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'ready as {client.user} with prefix "{bot_prefix}" on "{guild.name}" (id: {guild.id}).'
    )

    members = '\n -'.join([member.name for member in guild.members])
    print(f"guild members:\n -{members}")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='tes messages'))


@client.event
async def on_message():
    pass


@client.event
async def on_typing(channel, ashwokei, datetime):
    print(f"ashwokei is typing...")


@client.event
async def on_message(self, message):
    print(f"from: : ")
    if message.author == self.user:
        return


@client.event
async def on_message(message):
    if message.content.startswith("pouce"):
        channel = message.channel
        await channel.send("donne moi un 👍 stp")
        
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=20, check=check)
        except asyncio.TimeoutError:
            await channel.send("t'es nul 👎")
        else:
            await channel.send("merci 👍")


@client.command()
async def ping(ctx):
    await ctx.send(f"pong ({round(client.latency * 1000)}ms) {RandomEmoji()}")

@client.command(pass_context=True)          # join user's vc
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)


client.run(tok_data["pybot_token"])
