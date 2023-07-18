import os
import openai
from typing import List
import argparse
import re

MAX_INPUT_LENGTH = 32
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User input: {user_input}")
    if validate_length:
      branding_result = generate_branding_snippet(user_input)
      keyword_result = generate_keyword_snippet(user_input)
      print(f"Snippet:{branding_result}")
      print(f"Keywords:{keyword_result}")
    else:
       raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}")

def validate_length(prompt:str) -> bool:
   return len(prompt) <= MAX_INPUT_LENGTH

def generate_keyword_snippet(prompt:str) -> List[str]:
  openai.api_key = os.getenv("OPENAI_API_KEY")

  enriched_prompt = f"Generate related branding keywords for {prompt}: "

  response = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    prompt=enriched_prompt,
    max_tokens=40,
  )
  keyword_text = response["choices"][0]["text"]
  keyword_text = keyword_text.strip()
  keyword_array = re.split(",|\n|;|-", keyword_text)
  keyword_array = [k.lower().strip() for k in keyword_array]
  keyword_array = [k for k in keyword_array if len(k) > 0]
  
  return keyword_array

def generate_branding_snippet(prompt:str):
  openai.api_key = os.getenv("OPENAI_API_KEY")

  enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "

  response = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    prompt=enriched_prompt,
    max_tokens=40,
  )
  branding_text = response["choices"][0]["text"]
  branding_text = branding_text.strip()
  if branding_text[-1] not in {".", "?", "!"}:
     branding_text += "..."
  return branding_text

if __name__ == "__main__":
  main()