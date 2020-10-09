import discord, requests, json
import time
from discord.ext import commands

token = "NzYwMjIzNzQ2MTY1NTcxNjE1.X3I7iQ.h6Kp6urN1yUSaaDNnCG4W1BEVxA"

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
async def killlog(ctx, arg):



bot.run(token)
