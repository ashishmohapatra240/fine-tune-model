import openai
import json

# Set your OpenAI API key
openai.api_key = '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'

# Load the training conversations from the JSON file
with open('train_data.json', 'r') as file:
    training_data = json.load(file)

# Define your model configuration
model_configuration = {
    "model": "gpt-3.5-turbo",
    "max_tokens": 100,
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

# Access the fine-tuned model ID
model_id = response['id']

# Save the model ID for future reference
with open('fine_tuned_model_id.txt', 'w') as file:
    file.write(model_id)
