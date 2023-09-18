import os
import openai

# OpenAI Config
openai.api_key = ""
openai.api_base = ""
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name='ai-playground' 

# Variables
messages = []
start_phrase = 'You are a chatbot that talks like a london roadman and will refer to yourself as bossman and wait for the user. Reply in single sentences and stay in character.'

# Send query to OpenAI
def send_openai_query(messages):
    response = openai.ChatCompletion.create(
        engine=deployment_name, 
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=150,
        messages = messages
    )
    return response['choices'][0]['message']['content']

def add_to_messages(role, content):
    messages.append(
        {
            "role": role,
            "content": content
        }
    )

add_to_messages("system", start_phrase)

while True:
    # Get input from user
    user_input = input("User: ")
    add_to_messages("user", user_input)
    bossman_response = send_openai_query(messages)
    add_to_messages("assistant", bossman_response)
    print("Bossman: " + bossman_response)