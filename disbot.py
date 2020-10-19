import discord, requests, json
import time
from discord.ext import commands

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


@bot.command(pass_context=True)
async def killmails(ctx):
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
                await ctx.send(killlnk)
            else:
                print("no vic")
            time.sleep(1)



#@bot.command()
#async def killlog(ctx, arg):



bot.run(token)
