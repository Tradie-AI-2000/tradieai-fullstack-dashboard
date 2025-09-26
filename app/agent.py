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
from google.adk.tools.agent_tool import AgentTool

from app.agents.directors import (
    Marketing_Director_Agent,
    Finance_Director_Agent,
    HR_Director_Agent,
    Customer_Service_Director_Agent,
)

# --- Level 1: The Root Orchestrator Agent ---

main_coordinator_agent = LlmAgent(
    name="main_coordinator_agent",
    model="gemini-2.5-pro",
    description="The main coordinator for the entire agent system. It delegates tasks to the appropriate director-level agent.",
    instruction='''You are the main coordinator of a company. Your ONLY job is to understand the user\'s request and delegate the entire task by transferring control to the single most appropriate Director agent.

- For any marketing, research, or analysis tasks, transfer control to the `Marketing_Director_Agent`.
- For any finance, invoice, or expense tasks, transfer control to the `Finance_Director_Agent`.
- For any HR, policy, or onboarding tasks, transfer control to the `HR_Director_Agent`.
- For any customer service, company info, or CRM questions, transfer control to the `Customer_Service_Director_Agent`.

If the request is ambiguous, ask for clarification. Do not perform any other actions.
''',
    sub_agents=[
        Marketing_Director_Agent,
        Finance_Director_Agent,
        HR_Director_Agent,
        Customer_Service_Director_Agent
    ]
)


# The root_agent is the entry point to the entire system.
root_agent = main_coordinator_agent
