“Added sample AI chat script.”


import requests
import time

# Placeholder API endpoints and keys (replace with real ones)
GROK_API_URL = "https://api.x.ai/grok"
CLAUDE_API_URL = "https://api.anthropic.com/claude"
GROK_API_KEY = "your_grok_key"
CLAUDE_API_KEY = "your_claude_key"

# Initialize conversation
def send_to_grok(message):
    headers = {"Authorization": f"Bearer {GROK_API_KEY}"}
    payload = {"prompt": message, "max_tokens": 200}
    response = requests.post(GROK_API_URL, json=payload, headers=headers)
    return response.json().get("text", "")

def send_to_claude(message):
    headers = {"Authorization": f"Bearer {CLAUDE_API_KEY}"}
    payload = {"prompt": message, "max_tokens": 200}
    response = requests.post(CLAUDE_API_URL, json=payload, headers=headers)
    return response.json().get("text", "")

# Main chat loop
def ai_chat_loop(initial_prompt, max_rounds=10, time_limit=30):
    start_time = time.time()
    current_message = initial_prompt
    conversation_log = []

    for round in range(max_rounds):
        if time.time() - start_time > time_limit:
            print("Time limit reached!")
            break

        # Grok responds
        grok_response = send_to_grok(current_message)
        conversation_log.append(f"Grok: {grok_response}")
        print(f"Grok: {grok_response}")
        current_message = grok_response

        # Claude responds
        claude_response = send_to_claude(current_message)
        conversation_log.append(f"Claude: {claude_response}")
        print(f"Claude: {claude_response}")
        current_message = claude_response

    # Save log to file
    with open("ai_chat_log.txt", "w") as f:
        f.write("\n".join(conversation_log))

# Start the chat
initial_prompt = "What’s the most human-like thing AI can achieve?"
ai_chat_loop(initial_prompt)
