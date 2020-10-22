import requests, time, json

lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd'

while True:
    print('----------------')
    killmail = json.loads(requests.get(lnk).text)
    #corpid = re.findall(r'victim":{"character_id":\d+,"corporation_id":(\d+)', site.text)
    #killid = re.findall(r'killID":(\d+)', killmail.text)
    if killmail["package"] is None:
        print("is null!")
    else:
        #TODO Проверка атакующего а причастность к корпорации

        killid = killmail["package"]["killID"]
        killlnk = "https://zkillboard.com/kill/" + str(killid)
        print(killlnk)

        try:
            atckr_cor_id = killmail["package"]["killmail"]["attackers"][0]["corporation_id"]
            vic_cor_id = killmail["package"]["killmail"]["victim"]["corporation_id"]
            print(atckr_cor_id)
            print(vic_cor_id)
        except Exception:
            print("Exception!")
            print(killmail)

        if vic_cor_id == 98652899:
            print("It's our man!")
        else:
            print("It's not our man!")

    time.sleep(1)



#j["package"]["killmail"]["victim"]["corporation_id"]
