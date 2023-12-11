import discord
from discord import Interaction
import re
from discord.ext import commands
from discord.app_commands import CommandTree
from GPT import question
from dotenv import load_dotenv
import os

#.envファイルの読み込み
load_dotenv()

#TOKENを代入
TOKEN = os.environ['TOKEN']

#接続に必要なClientオブジェクトを作成
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
tree = CommandTree(client)
# 起動時に動作する処理
@client.event
async def on_ready():
  print("logged in")
  await tree.sync()
  
#メッセージの送受信
#@client.event
#async def on_message(message: discord.Message):
#  
#  #openaiAPIを叩くためのコマンド(大文字小文字問わない)
#  regex_pattern = r"/GPT (.+)"  
#  regex_match = re.match(regex_pattern, message.content, re.IGNORECASE) 
#  
#  #送信者がbotの場合は無視
#  if message.author.bot:
#    return
#  else:
#    if message.content.startswith("/hello"):
#      await message.channel.send("hello")
#    if regex_match:
#      print(message.content)
#      prompt = re.split(r"/gpt", message.content, flags=re.IGNORECASE)[1:]
#      ans = question(prompt)
#      await message.channel.send(ans)

@tree.command(name="hello", description="Helloを返す")
async def hello(interaction: Interaction):
  await interaction.response.send_message(f'Hello, {interaction.user.mention}')
  
@tree.command(name="gpt", description="ChatGPTが説明してくれる")
async def gpt(interaction: Interaction, prompt:str):
  print(prompt)
  ans = question(prompt)
  await interaction.response.send_message(ans)
  
client.run(TOKEN)
