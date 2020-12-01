import discord
import requests
import json
import datetime
import config
import asyncio


class MyClient(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create the background task and run it in the background
		self.bg_task = self.loop.create_task(self.my_background_task())

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def my_background_task(self):
		await self.wait_until_ready()
		channel = self.get_channel(config.channel_id)  # channel ID goes here
		while not self.is_closed():
			try:
				killmail = json.loads(requests.get(lnk).text)
				print("Request success")
				now = datetime.datetime.now()
				print("Time {}:{}:{}".format(now.hour, now.minute, now.second))
				if killmail["package"] is None:
					print("No new killmails.")
				else:
					killid = killmail["package"]["killID"]
					killlnk = "https://zkillboard.com/kill/" + str(killid)
					print(killlnk)

					try:
						for atk in killmail["package"]["killmail"]["attackers"]:
							if atk["corporation_id"] == config.corp_id:
								atckr_corp_id = atk["corporation_id"]

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

					if vic_corp_id == config.corp_id or atckr_corp_id == config.corp_id:
						print("It's our man!")
						await channel.send(killlnk)
					else:
						print("It's not our man!")
				print('----------------')
				await asyncio.sleep(1)
			except Exception:
				print("Request fail")
				await asyncio.sleep(5)


lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd_test'
client = MyClient()
client.run(config.token)
