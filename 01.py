import discord
from discord.ext import commands
import json

with open('setting.json','r', encoding='utf8') as jfile: #'r'是讀取的意思read 用'utf8'去解碼 jfile我命名的
    jdata = json.load(jfile)#jdata是變數

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> 你的珮珣已上線!! <<")

@bot.command()
async def 圖片(ctx):
    pic = discord.File("D:\\GitHub\\01_Bot\\pic\\1.jpg")
    await ctx.send(file= pic)

@bot.event
async def on_member_join(member):
    print(f'{member}出現囉!')#join(出現囉)

@bot.event
async def on_member_remove(member):
    print(f'{member}離開了!')#leave(離開了)  

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')   

bot.run(jdata['TOKEN'])
