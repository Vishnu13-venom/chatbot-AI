import openai
import os
openai.api_key = os.getenv("Enter your key")

openai.File.create(
  file=open("prompt_completion_pairs.json","rb"),
  purpose='fine-tune'
)