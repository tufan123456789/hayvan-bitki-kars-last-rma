import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def siniflandir(ctx):
    if ctx.message.attachments :
        # sınıflandırma işlemleri
        
        for attachment in ctx.message.attachments:
            name = attachment.filename
            url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Resmi şuraya kaydettiniz ./{attachment.filename}")
            
            await ctx.send("Sonucunuz yükleniyor..")
            # sınıflandırma sonucunu göstermek!!!!
            await ctx.send(get_class(model_path = "./keras_model.h5", labels_path = "./labels.txt", image_path = f"./{attachment.filename}" ))


    else:
        await ctx.send("Sınıflandırma için resim yükleyin...")


bot.run("MTIzNjM1OTcxNTQ2NzAzODcyMQ.GU7WAv.qaVR7ZAxHV92N2ivMi8f11o3m0xSEMyxRcCIuE")