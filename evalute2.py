import openai
import json
import os
from dotenv import load_dotenv

load_dotenv('api_key.env')

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load the training conversations from the JSON file
with open('new_data-8.json', 'r') as file:
    train_data = json.load(file)

# Define your model ID
model_id = os.getenv('chatcmpl-7XtOG33VPTgoWkWO1Mpk7SDG0LUBW')

# Define your model configuration
model_configuration = {
    "model": model_id,
    "temperature": 0.8,
    "max_tokens": 100,
    "engine": "davinci"  # or use "curie" if you have access to it
}

# Evaluate the model on the training set
total_examples = len(train_data) // 2  # Divide by 2 since we have user and assistant messages

correct_predictions = 0

user_input="What is Harpoon"

response = openai.Completion.create(
        engine=model_configuration['engine'],
        prompt=f"User: {user_input}\nAssistant:",
        temperature=model_configuration['temperature'],
        max_tokens=model_configuration['max_tokens'],
        model=model_configuration['model']
    )

print(response.choices[0].text.strip())