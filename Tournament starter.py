import discord
#import sqlite3
from bs4 import BeautifulSoup
import html
from datetime import date
from datetime import datetime
from datetime import timedelta
import requests

client = discord.Client()
riotkey = ""

@client.event
async def on_ready():
    print("Logged in as:\n\t%s\n\t%s\n\n" % (client.user.name, client.user.id))
    await client.change_presence(game=discord.Game(name=status))

@client.event
async def on_member_join(member):   
    await client.send_message(member.server, "Welcome %s to the server" % member.name)
@client.event
async def on_member_remove(member):
    await client.send_message(member.server, "%s has left or has been kicked!" % member.name)
@client.event
async def on_message(message):
	nowTime = datetime.now().strftime("%H:%M:%S")
	print("%s\n\t%s\t\n\t%s" % (nowTime,message.author,message.clean_content))
	command = message.content.split(" ")[0]
	if command == ("!tournament"):
		splitmsg = message.content.split(" ")
		if len(splitmsg) < 2:
			await client.send_message(message.channel, "Insert a tournament name!")
		else:
			payload = {'name':'{}'.format(splitmsg[1]), 'providerId' : '0'}
			url = "https://euw1.api.riotgames.com/lol/tournament/v3/tournaments?api_key={}".format(riotkey)
			r = request.post(url,data=json.dumps(payload))
			print(r.text)
			print(r.status_code)
			await client.send_message(message.channel,"Created a tournament match named {}".format(splitmsg[1]))

client.run('')