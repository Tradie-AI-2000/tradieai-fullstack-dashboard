
import vertexai
import vertexai.agent_engines
import os

# Set required environment variables for Vertex AI
os.environ["GOOGLE_CLOUD_PROJECT"] = "tradieai-fullstack-production"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

PROJECT_ID = "tradieai-fullstack-production"
LOCATION = "us-central1"
AGENT_ENGINE_ID_NUM = "4161770258387959808"

AGENT_ENGINE_ID = f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{AGENT_ENGINE_ID_NUM}"

print(f"Attempting to connect to agent: {AGENT_ENGINE_ID}")

try:
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    print("Vertex AI initialized.")

    remote_agent_engine = vertexai.agent_engines.get(AGENT_ENGINE_ID)

    print("Successfully retrieved remote agent engine.")
    print("Querying agent with 'hello'...")

    # Using stream_query as it's better for debugging real-time issues
    event_count = 0
    for event in remote_agent_engine.stream_query(message="hello", user_id="troubleshooting-user"):
        print("--- Event Received ---")
        print(event)
        event_count += 1

    if event_count == 0:
        print("\nQuery completed, but no events were received. The agent might be running but not producing output.")
    else:
        print(f"\nQuery completed. Received {event_count} events.")

except Exception as e:
    print(f"An error occurred: {e}")
