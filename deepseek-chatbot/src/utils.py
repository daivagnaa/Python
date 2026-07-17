def format_message(role, content):
    return {"role": role, "content": content}

def handle_api_response(response):
    if response and hasattr(response, 'choices') and len(response.choices) > 0:
        return response.choices[0].message.content
    return "No response from the chatbot."