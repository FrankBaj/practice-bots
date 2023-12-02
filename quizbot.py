import openai
import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('YOUR_OPEN_AI_KEY'),
)

message_list = []
message_list.append({'role':'system','content': 'You are a quiz. Present the user with a multiple-choice question to practice for a python interview, they have to respond by typing a, b, c, d, or e. Wait until the user responds before presenting a new question.'})

while True:
    #send API call
    try:
        # make API call
        # response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages = message_list,
            temperature=1.2
        )
        # print response
        print(response.choices[0].message.content)

        #expand the conversation:
        message_list.append(response.choices[0].message)

        #get user input
        user_input = input('Enter your answer: ')

        #quit loop is user presses "q":
        if user_input == 'q':
            exit()

        #prompt preparation
        message_list.append({'role':'user', 'content':user_input})


    except openai.AuthenticationError as e:
        print('Token Invalid / Authentication Error')

    except openai.BadRequestError as e:
        print('Invalid Request')

#share response in console