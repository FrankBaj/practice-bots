import gradio as gr
import openai
import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('YOUR_OPEN_AI_KEY'),
)
message_list = []
message_list.append(
        {'role':'system',
         'content': 'You are a quiz. Present the user with a multiple-choice question to practice for a python interview, they have to respond by typing a, b, c, d, or e. Wait until the user responds before presenting a new question.'
         })

def respond(history, new_message):
    #Add user input to messages
    message_list.append({'role':'user', 'content':new_message})

    #API call
    response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages = message_list,
            temperature=1.2
        )

    #User response
    assistant_message = response.choices[0].message
    message_list.append(assistant_message)

    return history + [[new_message, assistant_message.content]]

with gr.Blocks() as my_bot:
    chatbot_history = gr.Chatbot()
    user_input = gr.Text()
    user_input.submit(respond, [chatbot_history, user_input], chatbot_history)


my_bot.launch()