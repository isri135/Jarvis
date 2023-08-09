import openai
from speechToText import get_speech_input

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    message = get_speech_input()
    if message == "q":
        break
    
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
