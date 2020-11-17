import discord
import requests
import json
import datetime
import time
from discord.ext import commands
####
print("Script started")
token = ""
bot = commands.Bot(command_prefix='!') #инициализация бота

@bot.command(pass_context=True)
async def test(ctx, arg):
	await ctx.send(arg)

@bot.command(pass_context=True)
async def hello(ctx):
	author = ctx.message.author
	await ctx.send(f'Hello, {author.mention}')

@bot.command()
async def fox(ctx,arg):
	iarg=int(arg)
	while iarg>0:
		response = requests.get('https://some-random-api.ml/img/fox') # Get-запр    ос
		json_data = json.loads(response.text) # Извлекаем JSON
		embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
		embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
		await ctx.send(embed = embed) # Отправляем Embed
		time.sleep(1)
		iarg=iarg-1
		print(iarg)

@bot.command()
async def kms(ctx): # killmails
	#@bot.event
	#async def on_connect(ctx):
	print("Connetted! Start recieving killmail's.")
	lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd_test'
	while True:
		try:
			killmail = json.loads(requests.get(lnk).text)
			print("Request success")
			now = datetime.datetime.now()
			print("Time {}:{}:{}".format(now.hour, now.minute, now.second))
			# corpid = re.findall(r'victim":{"character_id":\d+,"corporation_id":(\d+)', site.text)
			# killid = re.findall(r'killID":(\d+)', killmail.text)
			if killmail["package"] is None:
				print("No new killmails.")
			else:
				killid = killmail["package"]["killID"]
				killlnk = "https://zkillboard.com/kill/" + str(killid)
				print(killlnk)

				try:
					atckr_corp_id = killmail["package"]["killmail"]["attackers"][0]["corporation_id"]
					print('Attacker corp_id:', atckr_corp_id)
				except Exception:
					atckr_corp_id = 0
					print("Exception! Attacker is not a member of a corporation.")

				try:
					vic_corp_id = killmail["package"]["killmail"]["victim"]["corporation_id"]
					print('Victim corp_id:', vic_corp_id)
				except Exception:
					vic_corp_id = 0
					print('Exception! Victim is mot a member of a corporation.')

				if vic_corp_id > 0 or atckr_corp_id > 0:
					print("It's our man!")
					await ctx.send(killlnk)
				else:
					print("It's not our man!")
			print('----------------')
			time.sleep(1)

		except Exception:
			print("Request fail")
			time.sleep(5)
			break

bot.run(token)
