import openai
import json
import os
from dotenv import load_dotenv


load_dotenv('api_key.env')
# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load the training conversations from the JSON file
# with open('convs.json', 'r') as file:
#     training_data = json.load(file)

f=open('convs-2.json')
training_data=json.load(f)

# Define your model configuration
model_configuration = {
    "model": "gpt-3.5-turbo",
    "max_tokens": 2500,
    "temperature": 0.8,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

# Fine-tune the model
response = openai.ChatCompletion.create(
    messages=training_data,
    **model_configuration
)

print(response)

# Access the fine-tuned model ID
model_id = response['id']

# Save the model ID for future reference
with open('fine_tuned_model_id.txt', 'w') as file:
    file.write(model_id)
