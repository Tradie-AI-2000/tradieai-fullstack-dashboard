import vertexai.agent_engines
import json

PROJECT_ID = "tradieai-fullstack-production"
LOCATION = "us-central1"
AGENT_ENGINE_ID = f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/4161770258387959808"

print(f"Attempting to get remote agent with ID: {AGENT_ENGINE_ID}")
remote_agent_engine = vertexai.agent_engines.get(AGENT_ENGINE_ID)
print("Remote agent obtained. Sending a test query...")

# New marketing research task
message_content = "please research how i can successfully market to rugby clubs in nz and offer them AI consultancy services."

for event_dict in remote_agent_engine.stream_query(message=message_content, user_id="test_user"):
    if 'content' in event_dict and event_dict['content']:
        if 'parts' in event_dict['content'] and event_dict['content']['parts']:
            for part in event_dict['content']['parts']:
                if 'text' in part and part['text']:
                    print(part['text'], end="")
    print()
print("\n--- End of response ---")
