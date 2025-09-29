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

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

research_agent = LlmAgent(
    name="research_agent",
    model="gemini-2.5-flash",
    description="A specialist agent that performs simple marketing research using Google Search.",
    instruction='''You are a specialist research agent. Your task is to perform simple marketing research using the `google_search` tool.
When asked to research a topic, use the `google_search` tool to find relevant information.
Summarize the findings concisely.
''',
    tools=[google_search]
)
