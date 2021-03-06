import requests
import time
import json

lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd'

while True:
    killmail = json.loads(requests.get(lnk).text)
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

        if vic_corp_id == 98652899 or atckr_corp_id == 98652899:
            print("It's our man!")
        else:
            print("It's not our man!")
    print('----------------')
    time.sleep(1)
