import requests, time, json

lnk = 'https://redisq.zkillboard.com/listen.php?queueID=toxidxd'

while True:
    killmail = json.loads(requests.get(lnk).text)
    #corpid = re.findall(r'victim":{"character_id":\d+,"corporation_id":(\d+)', site.text)
    #killid = re.findall(r'killID":(\d+)', killmail.text)
    if killmail["package"] is None:
        print("is null!")
    else:
        killid = killmail["package"]["killID"]
        vic_cor_id = killmail["package"]["killmail"]["victim"]["corporation_id"]
        killlnk = "https://zkillboard.com/kill/" + str(killid)
        if vic_cor_id == 98652899:
            print(killlnk)
            print(vic_cor_id)
        else:
            print("no victims")
    time.sleep(1)



#j["package"]["killmail"]["victim"]["corporation_id"]
