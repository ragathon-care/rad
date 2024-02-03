from openai import OpenAI
import os

diffbot_token = os.environ.get("DIFFBOT_TOKEN")

client = OpenAI(api_key=diffbot_token, base_url="https://llm.diffbot.com/rag/v1/")
response = client.chat.completions.create(
     model="diffbot-medium",
     messages=[
         {
             "role": "user",
             "content": "Who is the CEO of Twitter?"
         }
     ],
     stream=False,
 )

print(response.choices[0].message.content)
