from openai import OpenAI

 client = OpenAI(api_key="YOUR_DIFFBOT_TOKEN", base_url="https://llm.diffbot.com/rag/v1/")
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