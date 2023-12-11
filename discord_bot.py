import discord
from discord import app_commands
from discord.ext import commands
import re
from GPT import question
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
tree = app_commands.CommandTree(client)


# 起動時に動作する処理
@client.event
async def on_ready():
  print("logged in")
  await tree.sync()
  
#メッセージの送受信
@client.event
async def on_message(message):
  
  #openaiAPIを叩くためのコマンド(大文字小文字問わない)
  regex_pattern = r"/GPT (.+)"  
  regex_match = re.match(regex_pattern, message.content, re.IGNORECASE) 
  
  #送信者がbotの場合は無視
  if message.author.bot:
    return
  else:
    if message.content.startswith("/hello"):
      await message.channel.send("Hello")
    if regex_match:
      print(message.content)
      prompt = re.split(r"/gpt", message.content, flags=re.IGNORECASE)[1:]
      ans = question(prompt)
      await message.channel.send(ans)
      
@tree.command(name="test",description="テストコマンドです。")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("てすと！",ephemeral=True)#ephemeral=True→「これらはあなただけに表示されています」

client.run(TOKEN)



