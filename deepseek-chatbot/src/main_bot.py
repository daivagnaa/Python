# filepath: deepseek-chatbot/src/main_bot.py

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.deepseek.com")

messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )
        reply = response.choices[0].message.content
        print("Bot:", reply)
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print("Error:", e)