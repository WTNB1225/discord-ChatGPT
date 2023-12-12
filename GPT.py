from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]

def question(prompt):
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "日本語を使用して回答してください"},
      {"role": "user", "content": prompt}
    ]
  )
  return completion.choices[0].message.content