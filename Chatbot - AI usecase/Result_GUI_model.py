import tkinter as tk
import openai

# Replace with your OpenAI API key
api_key = "Enter your key"

# Replace with your chat model ID
model_id = "ft:gpt-3.5-turbo-0613:brainlabs::7xdAGi9a"

def on_submit():
    # Get the user's message from the input field
    user_message = input_field.get()

    # Create a conversation message
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    # Make an API request to the chat model
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )

    # Get the assistant's reply
    assistant_reply = response.choices[0].message["content"]

    # Display the assistant's reply in the result text area
    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("end", assistant_reply)
    result_text.config(state="disabled")

    # Clear the input field
    input_field.delete(0, "end")

# Create the main window
window = tk.Tk()
window.title("Chat with AI")

# Create the input field and submit button
input_field = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=on_submit)

# Create the result text area
result_text = tk.Text(window, state="normal", width=80, height=20)

# Add widgets to the window
input_field.pack()
submit_button.pack()
result_text.pack()

# Run the main loop
window.mainloop()
