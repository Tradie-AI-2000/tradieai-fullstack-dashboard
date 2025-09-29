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

import asyncio
import logging

from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent


async def main():
    """Runs the agent with a sample query and prints the events."""
    logging.basicConfig(level=logging.INFO)
    session_service = InMemorySessionService()

    session = await session_service.create_session(user_id="test_user", app_name="test")
    runner = Runner(agent=root_agent, session_service=session_service, app_name="test")

    # Test with a finance-specific prompt
    message = types.Content(
        role="user", parts=[types.Part.from_text(text="Create an invoice for 'Globex Corp' for 1500 dollars.")]
    )

    print("--- Running agent with finance prompt ---")
    events = runner.run_async(
        new_message=message,
        user_id="test_user",
        session_id=session.id,
        run_config=RunConfig(streaming_mode=StreamingMode.SSE),
    )

    async for event in events:
        print(f"[EVENT] Author: {event.author}, Content: {event.content}, Actions: {event.actions}")

if __name__ == "__main__":
    asyncio.run(main())
