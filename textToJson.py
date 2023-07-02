import json

conversations = []

with open('conversations.txt', 'r') as file:
    lines = file.readlines()

user_lines = []
character_lines = []

for line in lines:
    if line.startswith("Max:"):
        if user_lines and character_lines:
            conversation = {
                "role": "user",
                "content": " ".join(user_lines)  # Join lines with a space
            }
            conversations.append(conversation)
            conversation = {
                "role": "character",
                "content": " ".join(character_lines)  # Join lines with a space
            }
            conversations.append(conversation)
            user_lines = []
            character_lines = []
        user_lines.append(line.strip()[len("Max: "):])
    elif line.startswith("Chumbucket:"):
        character_lines.append(line.strip()[len("Chumbucket: "):])

# Add the last conversation
if user_lines and character_lines:
    conversation = {
        "role": "user",
        "content": " ".join(user_lines)  # Join lines with a space
    }
    conversations.append(conversation)
    conversation = {
        "role": "character",
        "content": " ".join(character_lines)  # Join lines with a space
    }
    conversations.append(conversation)

# Save as JSON
with open('conversations.json', 'w') as file:
    json.dump(conversations, file, indent=4)
