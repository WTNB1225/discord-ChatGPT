import discord
from dotenv import load_dotenv
import os

#.envファイルの読み込み
load_dotenv()

#TOKENを代入
TOKEN = os.environ['TOKEN']


#接続に必要なClientオブジェクトを作成
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
  print("logged in")
  
#メッセージの送受信
@client.event
async def on_message(message):
  #送信者がbotは無視
  if message.author.bot:
    return
  if message.content == "/hello":
    await message.channel.send("Hello")
client.run(TOKEN)



