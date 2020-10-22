import requests, time, json

lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd'

while True:
    print('----------------')
    killmail = json.loads(requests.get(lnk).text)
    #corpid = re.findall(r'victim":{"character_id":\d+,"corporation_id":(\d+)', site.text)
    #killid = re.findall(r'killID":(\d+)', killmail.text)
    if killmail["package"] is None:
        print("No new killmails.")
    else:
        killid = killmail["package"]["killID"]
        killlnk = "https://zkillboard.com/kill/" + str(killid)
        print(killlnk)

        try:
            atckr_corp_id = killmail["package"]["killmail"]["attackers"][0]["corporation_id"]
            print(atckr_corp_id)
        except Exception:
            atckr_corp_id = 0
            print("Exception! Attacker is not a member of a corporation.")

        try:
            vic_corp_id = killmail["package"]["killmail"]["victim"]["corporation_id"]
            print(vic_corp_id)
        except Exception:
            vic_corp_id = 0
            print('Exception! Victim is mot a member of a corporation.')

        if vic_corp_id == 98652899 or atckr_corp_id == 98652899:
            print("It's our man!")
        else:
            print("It's not our man!")

    time.sleep(1)



#j["package"]["killmail"]["victim"]["corporation_id"]
