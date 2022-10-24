import discord
import re
import random
token = "lol nice try"
reader = open("./token.key")
token = reader.readline()

# Variables
# todo: bot was released in 2016, need to update

intents = discord.Intents.default()
intents.typing = False
intents.message_content = True
intents.presences = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    serverlist = str(discord.guild)
    print(serverlist)

@client.event
async def on_message(message):

    if message.content.startswith('diceroll') or message.content.startswith('!dr'):
        aStr = message.content
        dicePattern = re.findall(r'([0-9]{1,5}d)', aStr)
        sidesPattern = re.findall(r'(d[0-9]{1,5})', aStr)
        adderPatter = re.finditer(r'([\+|\-][0-9]{1,5})', aStr)
        messageResponsePrefix = f"{message.author.mention} rolled "
        totalTotal = 0
        for numDice, numSides in zip(dicePattern, sidesPattern):
            messageResponse = messageResponsePrefix
            totalRolled = 0
            for x in range(0, int(numDice[0:-1])):
                aRoll = random.randint(1, int(numSides[1:]))
                totalRolled += aRoll
                messageResponse += f"{aRoll}, "
            messageResponse += f' for a total of {totalRolled}.'
            totalTotal += totalRolled
            messageMaxLen = 1999
            if len(messageResponse) > messageMaxLen:
                while len(messageResponse) > messageMaxLen:
                    messageSubSection = messageResponse[0:messageMaxLen]
                    messageResponse = messageResponse[messageMaxLen:]
                    await message.channel.send(messageSubSection)
            await message.channel.send(messageResponse)
        await message.channel.send(f"{message.author.mention} rolled a final total of {totalTotal}.")

client.run(token)
