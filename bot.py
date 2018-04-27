

import todoist
import discord
import sqlite3
import random
import asyncio
import requests
import datetime
from discord import Game
from discord.ext.commands import Bot
from trello import TrelloClient

BOT_PREFIX = ("?", "!",";")
TOKEN = '[TOKEN_HERE]'

client = Bot(command_prefix=BOT_PREFIX)

conn = sqlite3.connect('lists.db')
cur = conn.cursor()

try:
    cur.execute( """CREATE TABLE HouseShoppingList (
                store TEXT,
                qnt REAL,
                item TEXT,
                requestee TEXT
                
                )""" )
except:
    pass


@client.command(name='ChoresRulet',
                description="assigns chores.",
                brief="Answers from the beyond.",
                aliases=['spin',],
                pass_context=True)
async def todo(context):
    possible_responses = [
        'take out the trash',
        'vaccume',
        'do dishes',

    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
##read message and reply with same message##
# @client.command(pass_context=True)
# async def test(ctx, store, *, args):
#
#     await client.say("buy " + args + " at " + store)

@client.command(pass_context=True,
                name="list",)
async def list_(ctx, *, arg):
    args = arg.split(" ") # split argument into list
    action = args[0] # Take first word of argument as action
    store = args[1] # take second word as store name
    item = " ".join(args[2:]) #join the rest of the argument and use as item
    filename = 'list-' + store + '.txt'

    Lists = []
    with open("lists.txt", 'r') as f:
        Lists = f.read().splitlines()
        print(Lists)

    if filename not in Lists :
        Lists.append (filename)
        with open(filename, 'a') as file_object:
            file_object.write(filename + "\n")
        with open("lists.txt", 'w') as f:
            for items in Lists:
                f.write("%s\n" % items)
        print(Lists)

    if action == 'add' :
        with open(filename, 'a') as file_object:
            file_object.write("\n" + item + " " + str(ctx.message.author))

    if action == 'show' :
        if store == 'all' :
            await client.say(str(Lists))
        else:
            with open(filename, 'r') as file_object:
                gList=file_object.readlines()
                await client.say( "```\n" + str(gList) + "\n```" )


    await client.say(item + " added to " + store + " " + str(ctx.message.author))


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




@client.command()
async def day():
    today = datetime.date.today()
    weekday = today.weekday()
    def f(x):
        return {
            0 : 'Monday',
            1 : 'Tuesday',
            2 : 'Wednsday',
            3 : 'Thuresday',
            4 : 'Friday',
            5 : 'Saturday',
            6 : 'Sunday',
        }[x]
    day = f(weekday)
    await client.say(day)


@client.command(pass_context=True)
async def xkcd(ctx, num=""):
    await client.say("https://xkcd.com/"+num+"/")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
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
            print(server.name)
            print("Current members:")
            for member in server.members:
                print(member.name)

        await asyncio.sleep(6000)




client.loop.create_task(list_servers())
client.run(TOKEN)
