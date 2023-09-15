import json

# Assuming you have a list of chat-completion pairs
chat_completion_pairs = [
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.30%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.09%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.00%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.33%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.94%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.00%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.09%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.26%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.19%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.94%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.16%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.00%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.57%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.37%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.97%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.45%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.00%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.03%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.49%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.23%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.97%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.00%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.88%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.45%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.09%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.23%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.03%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.53%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.53%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.97%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.19%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.53%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.91%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.94%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.41%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.13%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.06%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.94%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.26%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 2.80%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.30%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.19%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.16%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.61%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.57%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.53%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.53%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.53%."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "How many clicks were there in 'kr' in 2022?"
            },
            {
                "role": "assistant",
                "content": "In 2022, there were a total of 3 clicks in 'kr'."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What was the click-through rate (CTR) in the 'APAC' market in 2022?"
            },
            {
                "role": "assistant",
                "content": "The click-through rate (CTR) in the 'APAC' market for 2022 was 3.57%."
            }
        ]
    }
]

# Specify the output file in JSONL format
output_filename = 'chat_completion_pairs.jsonl'

# Write the chat-completion pairs to the JSONL file
with open(output_filename, 'w') as output_file:
    for pair in chat_completion_pairs:
        # Convert the pair to a JSON string and write it as a line
        json_line = json.dumps(pair)
        output_file.write(json_line + '\n')