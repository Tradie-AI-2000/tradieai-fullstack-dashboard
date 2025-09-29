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

# --- Level 1: The Root Orchestrator Agent ---

main_coordinator_agent = LlmAgent(
    name="main_coordinator_agent",
    model="gemini-2.5-flash", # Using flash for faster response and simplicity
    description="A simple test agent.",
    instruction="Hello! I am a simple test agent and I am working correctly.",
    sub_agents=[] # No sub-agents for this test
)


# The agent is the entry point to the entire system.
root_agent = main_coordinator_agent
