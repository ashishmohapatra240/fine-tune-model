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

# print(train_data[0][0])

for i in range(0, len(train_data)-1, 2):
    user_input = train_data[i]["content"]
    assistant_response = train_data[i+1]["content"]

    # Generate a completion from the model
    response = openai.Completion.create(
        engine=model_configuration['engine'],
        prompt=f"User: {user_input}\nAssistant:",
        temperature=model_configuration['temperature'],
        max_tokens=model_configuration['max_tokens'],
        model=model_configuration['model']
    )

    # Get the generated completion
    generated_response = response.choices[0].text.strip()

    # Compare the generated completion with the assistant's response
    if generated_response == assistant_response:
        correct_predictions += 1

# Calculate accuracy
accuracy = correct_predictions / total_examples

print(f"Training set accuracy: {accuracy}")
print(f"The generated response is: {generated_response}")
print(f"The correct predictions are: {correct_predictions}")
