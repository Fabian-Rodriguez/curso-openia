import openai
import os
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())

openai.api_kei=os.getenv('OPENAI_API_KEY')
print(openai.api_kei)

def get_completion(prompt, model=" gpt—3 .5—turbo" ):
    messages= [{"role": "user", "content" : prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of
    )
    return response.choices[0] .message["content"]