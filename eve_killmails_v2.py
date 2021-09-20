import discord
import requests
import json
import datetime
import config
import asyncio

client = discord.Client()

@client.event
async def on_connect():
    print('Bot connected')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(channel_id)
    while True:
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
                        if atk["corporation_id"] == corp_id:
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

            print('----------------')
            await asyncio.sleep(0.2)
        except Exception:
            print("Request fail")
            await asyncio.sleep(5)

lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd'
channel_id = config.channel_id
corp_id = config.corp_id
client.run(config.token)
