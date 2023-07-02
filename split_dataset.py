import json
from sklearn.model_selection import train_test_split

# Load the conversations from the JSON file
with open('conversations.json', 'r') as file:
    conversations = json.load(file)

# Split the dataset into training and validation sets
train_data, val_data = train_test_split(conversations, test_size=0.2, random_state=42)

# Save the training set as JSON
with open('train_data.json', 'w') as file:
    json.dump(train_data, file, indent=4)

# Save the validation set as JSON
with open('val_data.json', 'w') as file:
    json.dump(val_data, file, indent=4)
