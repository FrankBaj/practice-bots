from openai import OpenAI
import openai
import wikipedia
import os

# pass api key
# NEVER upload key to Github
client = OpenAI(
    api_key = os.environ.get('YOUR_OPEN_AI_KEY'),
)

#get user input
input_title = input('Wikipedia Page Title: ')

#get wikipedia content
page = wikipedia.page(title=input_title, auto_suggest=False)

# define prompt
prompt = 'Create a 5-bullet point summary of: ' + page.content
messages_list = []
messages_list.append({'role': 'user', 'content':prompt})

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