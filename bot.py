

import todoist
import discord
import random
import asyncio
import requests
import datetime
from discord import Game
from discord.ext.commands import Bot
from item import Item
from trello import TrelloClient

BOT_PREFIX = ("?", "!", ";")
TOKEN = 'DISCORD_TOKEN_HERE'

client = Bot(command_prefix=BOT_PREFIX)





@client.command(name='ChoresRulet',
                description="",
                brief="",
                aliases=['spin', ],
                pass_context=True)

async def todo(context):
    possible_responses = [
        'take out the trash',
        'vaccume',
        'do dishes',

    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(pass_context=True,
                name="list",)
async def list_(ctx, action, *, arg):
    newItem = Item.from_string(arg, str(ctx.message.author))
    await client.say(newItem.__dict__)


    # Lists = []
    # with open("lists.txt", 'r') as f:
    #     Lists = f.read().splitlines()
    #     print(Lists)
    #
    # if filename not in Lists :
    #     Lists.append (filename)
    #     with open(filename, 'a') as file_object:
    #         file_object.write(filename + "\n")
    #     with open("lists.txt", 'w') as f:
    #         for items in Lists:
    #             f.write("%s\n" % items)
    #     print(Lists)
    #
    # if action == 'add' :
    #     with open(filename, 'a') as file_object:
    #         file_object.write("\n" + item + " " + str(ctx.message.author))
    #
    # if action == 'show' :
    #     if store == 'all' :
    #         await client.say(str(Lists))
    #     else:
    #         with open(filename, 'r') as file_object:
    #             gList=file_object.readlines()
    #             await client.say( "```\n" + str(gList) + "\n```" )
    #
    #
    # await client.say(item + " added to " + store + " " + str(ctx.message.author))


    # class gList(Object)
    #     function
    #         add(api_args)
    #             try:
    #                 try:
    #                     quantity = int(api_args[0])
    #                 catch:
    #                     quantity = int(api_args[0][:-1])
    #                 api_args.pop(obj=api_args[0])
    #
    #             catch:
    #                 quantity = 1
    #
    #
    #             item = ""
    #             while (api_args.length and api_args[0][0] != "("):
    #                 item += " " + api_args[0].copy
    #                 api_args.pop(obj=api_args[0])
    #             description = ""
    #             if api_args.length:
    #                 description = " ".join(api_args)
    #             return quantity, item, description




# @client.command()
# async def day():
#     today = datetime.date.today()
#     weekday = today.weekday()
#     def f(x):
#         return {
#             0 : 'Monday',
#             1 : 'Tuesday',
#             2 : 'Wednsday',
#             3 : 'Thuresday',
#             4 : 'Friday',
#             5 : 'Saturday',
#             6 : 'Sunday',
#         }[x]
#     day = f(weekday)
#     await client.say(day)


@client.command(pass_context=True)
async def xkcd(ctx, num=""):
    await client.say("https://xkcd.com/"+num+"/")

@client.event
async def on_ready():
    possible_responses = [
        'Vinkensport',
        'Segway Polo',
        'Yukigassen',
        '100 Blank White Cards!',
        'Doodle or Die',

    ]
    await client.change_presence(game=Game(name=random.choice(possible_responses)))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print('\t' + server.name)
            print("\tCurrent members:")
            for member in server.members:
                print('\t\t' + member.name)

        await asyncio.sleep(6000)

# async def trashday_reminder():
#     await client.wait_until_ready()
#     while not client.is_closed:
#         if datetime.date.today() == 2 :
#             await client.say("Trash day! @everyone")
#         await asyncio.sleep(3600*4)




client.loop.create_task(list_servers())
client.run(TOKEN)
