#!/usr/bin/env python
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from app.agent import root_agent
from app.agent_engine_app import AgentEngineApp


def main():
    """Runs the agent with a sample query and prints the author of each event."""
    logging.basicConfig(level=logging.INFO)
    print("--- Initializing Agent for Isolated Test ---")
    agent_app = AgentEngineApp(agent=root_agent)
    agent_app.set_up()

    # Test with a finance-specific prompt
    message = "Create an invoice for 'Globex Corp' for 1500 dollars."
    print(f"--- Running agent with prompt: '{message}' ---")

    # Get the generator for the events
    events_generator = agent_app.stream_query(message=message, user_id="test_user")

    # Manually iterate through the generator
    for event in events_generator:
        author = event.get("author", "N/A")
        content = event.get("content", {})
        print(f"[EVENT] Author: {author}")
        if content:
            print(f"        Content: {content}")

    print("--- Test Complete ---")

if __name__ == "__main__":
    main()