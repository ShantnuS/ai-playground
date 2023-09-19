import os
import openai
import requests

# OpenAI Config
openai.api_key = ""
openai.api_base = ""
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name='ai-playground' 

messages = []
example_response = '[{"question":"What is the capital of France?","choices":["London","Paris","New York","Dublin"],"answer":"Paris"},{"question":"What is the capital of India?","choices":["New Delhi","London","New York","Dublin"],"answer":"New Delhi"},{"question":"What is the capital of United Kingdom?","choices":["New Delhi","London","New York","Dublin"],"answer":"London"},{"question":"What is the capital of Germany?","choices":["Berlin","London","New York","Dublin"],"answer":"Berlin"},{"question":"What is the capital of Nepal?","choices":["New Delhi","London","Kathmandu","Dublin"],"answer":"Kathmandu"}]'
start_phrase = '''You will be given a wikipedia article and your task is to come up with 5 multiple choice questions based on the contents of that article for a quiz. 
            You are acting as an API and hence the response must be in full and in valid JSON and must not include any other text. 
            An example response is: {example_response}
            '''.format(example_response=example_response)

# Send query to OpenAI
def send_openai_query(messages):
    response = openai.ChatCompletion.create(
        engine=deployment_name, 
        temperature=0.4,
        max_tokens=500,
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

# Get Questions and Answers
def get_questions_and_answers(wiki_url):
    add_to_messages("user", "The wikipedia article is: " + wiki_url)
    response = send_openai_query(messages)
    return response

add_to_messages("system", start_phrase)
wiki_url = input("Wiki Article: ")
print(get_questions_and_answers(wiki_url))