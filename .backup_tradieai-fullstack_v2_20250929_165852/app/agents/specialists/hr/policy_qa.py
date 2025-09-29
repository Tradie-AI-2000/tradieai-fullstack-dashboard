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

import os
import glob

from google.adk.agents import LlmAgent

def find_policy_document(policy_name: str) -> str:
    """Searches for and retrieves the content of a company policy document."""
    search_pattern = os.path.join("policies", f"*{policy_name.replace(' ', '_')}*.md")
    found_files = glob.glob(search_pattern)

    if not found_files:
        return f"Could not find any policy document matching '{policy_name}'."

    try:
        with open(found_files[0], "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        return f"Error: Failed to read policy document {found_files[0]}. Reason: {e}"

policy_qa_agent = LlmAgent(
    name="policy_qa_agent",
    model="gemini-2.5-flash",
    description="Use this agent to answer questions about company policies.",
    instruction="Use the `find_policy_document` tool to find the relevant policy document and answer the user's question.",
    tools=[find_policy_document]
)
