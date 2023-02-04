# this is a test file for interacting with openai's api

import openai
import os

# get the API key from the .env file
from dotenv import load_dotenv

# see .env.example for more info
load_dotenv()
openai.api_key = os.getenv("API_KEY")

# Define the prompt
prompt = "What is the capital of France?"

# Use the Completion API to generate text based on the prompt
model_engine = "text-davinci-003"
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated text
message = completion.choices[0].text
print(message)