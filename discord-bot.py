import discord
from discord import Interaction
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
  
@tree.command(name="hello", description="Helloを返す")
async def hello(interaction: Interaction):
  print("hello")
  await interaction.response.send_message(f'Hello, {interaction.user.mention}')
  
@tree.command(name="gpt", description="ChatGPTが説明してくれる")
async def gpt(interaction: Interaction, prompt:str):
  await interaction.response.defer()
  print(prompt)
  ans = question(prompt)
  print(ans)
  embed = discord.Embed(title=prompt,description=ans,color=0xff0000) #16進数カラーコード
  await interaction.followup.send(f"{interaction.user.mention}", embed=embed)

@tree.command(name="delete_all", description="channelの会話を全て削除")
async def delete_all(interaction: Interaction):
  channel = interaction.channel
  await channel.purge()
client.run(TOKEN)
