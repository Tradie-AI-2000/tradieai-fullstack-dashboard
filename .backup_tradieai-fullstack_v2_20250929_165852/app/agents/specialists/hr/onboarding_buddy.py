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

def get_onboarding_info(new_hire_name: str) -> str:
    """Gets onboarding information for a new hire from a file."""
    try:
        with open("onboarding/new_hire_guide.md", "r", encoding="utf-8") as f:
            guide_content = f.read()
        return f"Welcome, {new_hire_name}! Here is some information to get you started:\n\n{guide_content}"
    except FileNotFoundError:
        return "Error: The new_hire_guide.md file was not found."
    except Exception as e:
        return f"An error occurred while fetching onboarding information: {e}"

onboarding_buddy_agent = LlmAgent(
    name="onboarding_buddy_agent",
    model="gemini-2.5-flash",
    description="Use this agent to get onboarding information for new employees.",
    instruction="Use the `get_onboarding_info` tool to provide onboarding information for the new hire.",
    tools=[get_onboarding_info]
)

