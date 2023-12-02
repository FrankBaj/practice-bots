from openai import OpenAI
import openai
import os

# pass api key
# NEVER upload key to Github
client = OpenAI(
    api_key = os.environ.get('YOUR_OPEN_AI_KEY'),
)

# define prompt
messages_list = []
messages_list.append({'role': 'system', 'content': 'You are personal assistant, whose role is to politely provide answers and generate further discussion.'})
messages_list.append({'role': 'user', 'content': 'Provide a short summary for the book: The Old Man and the Sea'})

try:
    # make API call
    # response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages = messages_list,
        temperature=1.2
    )
    # print response
    print(response.choices[0].message.content)

except openai.AuthenticationError as e:
    print('Token Invalid / Authentication Error')

except openai.BadRequestError as e:
    print('Invalid Request')