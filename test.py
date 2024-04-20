from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = ""
response = completion(
    model="gemini/gemini-1.5-pro-latest", 
    messages=[{"role": "user", "content": "how do you debug an ml model"}]
)

print(response.choices[0].message.content)

