import openai
import json

# Set your OpenAI API key
openai.api_key = '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'

# Load the validation conversations from the JSON file
with open('val_data.json', 'r') as file:
    validation_data = json.load(file)

# Define your model ID
model_id = 'chatcmpl-7Xly11UpdA21vveiO3TuAo3w9pt2U'

# Define your model configuration
model_configuration = {
    "model": model_id,
    "temperature": 0.8,
    "max_tokens": 100
}

# Evaluate the model on the validation set
total_examples = len(validation_data)
correct_predictions = 0

for conversation in validation_data:
    user_input = conversation[0]['content']
    assistant_response = conversation[1]['content']

    # Generate a completion from the model
    response = openai.Completion.create(
        model=model_configuration['model'],
        temperature=model_configuration['temperature'],
        max_tokens=model_configuration['max_tokens'],
        prompt=user_input
    )

    # Get the generated completion
    generated_response = response.choices[0].text.strip()

    # Compare the generated completion with the assistant's response
    if generated_response == assistant_response:
        correct_predictions += 1

# Calculate accuracy
accuracy = correct_predictions / total_examples

print(f"Validation set accuracy: {accuracy}")