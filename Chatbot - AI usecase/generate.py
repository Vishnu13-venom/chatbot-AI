import csv
import json

# Load your CSV data
with open('sample_data .csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    data_rows = list(csv_reader)

# Define a function to create prompt and completion pairs
def create_prompt_completion(row):
    # Customize this function based on your specific use case and dataset
    # For example, you might create prompts that ask questions about the data
    prompt = f"What are the 'Clicks' and 'Cost (USD)' for the date {row['Date']} in {row['Country']}?"
    completion = f"The 'Clicks' for {row['Date']} are {row['Clicks']} and the 'Cost (USD)' is {row['Cost (USD)']}."
    return {"prompt": prompt, "completion": completion}

# Create prompt and completion pairs for each row in the dataset
prompt_completion_pairs = []
for row in data_rows:
    prompt_completion_pairs.append(create_prompt_completion(row))

# Save the prompt-completion pairs to a JSON file
with open('prompt_completion_pairs.json', 'w') as output_file:
    json.dump(prompt_completion_pairs, output_file, indent=4)

print(f"Generated {len(prompt_completion_pairs)} prompt-completion pairs.")
