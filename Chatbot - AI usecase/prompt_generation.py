import csv
import json

# Load your CSV data
csv_filename = 'sample_data .csv'
chat_completion_pairs = []

with open(csv_filename, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Pair 1: User Asks About Clicks in a Specific Country
        user_message_1 = f"How many clicks were there in '{row['Country']}' in 2022?"
        clicks_2022 = row['Clicks']
        assistant_response_1 = f"In 2022, there were a total of {clicks_2022} clicks in '{row['Country']}'."

        # Pair 2: User Inquires About the CTR in a Market
        user_message_2 = f"What was the click-through rate (CTR) in the '{row['Market']}' market in 2022?"
        ctr_2022 = row['CTR']
        assistant_response_2 = f"The click-through rate (CTR) in the '{row['Market']}' market for 2022 was {ctr_2022}."



        # Convert to chat-completion format and append to the list
        chat_completion_pairs.append({
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message_1},
                {"role": "assistant", "content": assistant_response_1}
            ]
        })
        
        chat_completion_pairs.append({
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message_2},
                {"role": "assistant", "content": assistant_response_2}
            ]
        })
        
        

# Save the list of chat and completion pairs to a JSON file
output_filename = 'chat_completion_pairs.json'
with open(output_filename, 'w') as output_file:
    json.dump(chat_completion_pairs, output_file, indent=4)

# Print a message indicating the number of chat-completion pairs generated
print(f"Generated {len(chat_completion_pairs)} chat-completion pairs.")
