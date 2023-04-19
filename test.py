import os
import openai

f = open("Secrets/Key.txt", "r")
key=f.read()
#print(key)
openai.api_key = key

response = openai.Completion.create(model="text-davinci-003", prompt="Write a peom about Weather", temperature=0, max_tokens=7)
print(response.choices[0].text)