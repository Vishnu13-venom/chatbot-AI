import openai

# Define your OpenAI API key
api_key = "Enter your key"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define your fine-tuned model ID
model_id = "ft:gpt-3.5-turbo-0613:brainlabs::7xdAGi9a"

# Load your evaluation data (messages with roles and content)
evaluation_data =  [
    {
        "role": "user",
        "content": "How many clicks were there in 'kr' in 2022?"
    },
    {
        "role": "assistant",
        "content": "In 2022, there were a total of 30 clicks in 'kr'."
    },
    {
        "role": "user",
        "content": "What's the capital of France?"
    },
    {
        "role": "assistant",
        "content": "The capital of France is Paris."
    },
    {
        "role": "user",
        "content": "Who wrote 'Romeo and Juliet'?"
    },
    {
        "role": "assistant",
        "content": "William Shakespeare wrote 'Romeo and Juliet'."
    },
    # Add more evaluation samples as needed
]

# Function to generate responses using the fine-tuned model
def generate_response(messages):
    completion = openai.ChatCompletion.create(
        model=model_id,
        messages=messages
    )
    return completion.choices[0].message["content"].strip()

# Evaluate accuracy
correct_count = 0
total_count = len(evaluation_data) // 2  # Divide by 2 because each sample has a user and assistant message

for i in range(0, len(evaluation_data), 2):
    user_message = evaluation_data[i]
    assistant_message = evaluation_data[i + 1]
    
    # Generate a response using your fine-tuned model
    generated_response = generate_response([user_message, assistant_message])

    # Compare the generated response to the assistant's response
    if generated_response == assistant_message["content"]:
        correct_count += 1

# Calculate accuracy
accuracy = (correct_count / total_count) * 100

print(f"Accuracy: {accuracy:.2f}%")
