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
		channel = self.get_channel(channel_id)  # channel ID goes here
		alarm = self.get_channel(alarm_id)
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
						atckr_corp_id = 0
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

					if vic_corp_id == corp_id or atckr_corp_id == corp_id:
						print("It's our man!")
						await channel.send(killlnk)
					else:
						print("It's not our man!")

					##################
					#ss_id = killmail["package"]["killmail"]["solar_system_id"]
					#print("Solar system", ss_id)
					#for sol in solars:
					#	if sol[0] == ss_id:
					#		print('alarm')
					#		print("kill in ", sol[1], " ", sol[2])
					#		alarm_message = "Kill in " + sol[1] + ", " + sol[2] + "!"
					#		await alarm.send(alarm_message)
					#		await alarm.send(killlnk)

				print('----------------')
				await asyncio.sleep(0.2)
			except Exception:
				print("Request fail")
				await asyncio.sleep(5)


lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd_test'
corp_id = config.corp_id
channel_id = config.channel_id
alarm_id = config.alarm_id
solars = [
	[30001972, '5-9WNU', '0 jumps'],
	[30001975, '12YA-2', '1 jump'],
	[30001976, 'BDV3-T', '2 jumps'],
	[30001998, 'WW-KGD', '3 jumps'],
	[30001999, 'XQ-PXU', '4 jumps'],
	[30002000, 'M-YCD4', '5 jumps'],
	[30002001, 'Q-5211', '6 jumps'],
	[30002003, 'CR-AQH', '5 jumps'],
	[30002002, 'R-2R0G', '6 jumps'],
	[30001991, 'ION-FG', '3 jumps'],
	[30001992, 'C-H9X7', '5 jumps'],
	[30001993, 'A8I-C5', '6 jumps'],
	[30001994, 'DK-FXK', '7 jumps'],
	[30001996, 'ZJET-E', '8 jumps'],
	[30001995, 'M-76XI', '8 jumps'],
	[30001997, 'U-INPD', '7 jumps'],
	[30001970, 'EL8-4Q', '1 jump'],
	[30001971, 'JC-YX9', '2 jumps'],
	[30001974, 'N-H32Y', '2 jumps'],
	[30001969, 'KI-TL0', '2 jumps'],
	[30001973, 'XI-VUF', '3 jumps'],
	[30001968, 'D7T-C0', '3 jumps'],
	[30002004, '8S-0E1', '4 jumps'],
	[30002005, '5ZXX-K', '5 jumps'],
	[30002006, 'JE-D5U', '6 jumps'],
	[30002008, 'OE-9UF', '7 jumps'],
	[30002009, 'PFU-LH', '7 jumps'],
	[30002007, '2-6TGQ', '6 jumps'],
	[30001965, '2D-0SO', '4 jumps'],
	[30001966, 'UR-E6D', '5 jumps'],
	[30001964, 'O-BY0Y', '5 jumps'],
]
client = MyClient()
client.run(config.token)
