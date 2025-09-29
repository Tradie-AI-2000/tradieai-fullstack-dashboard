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

from app.agents.specialists.hr import (
    policy_qa_agent,
    onboarding_buddy_agent,
)

HR_Director_Agent = LlmAgent(
    name="HR_Director_Agent",
    model="gemini-2.5-pro",
    description="Manages all Human Resources tasks, like policy questions and employee onboarding.",
    instruction='''You are the HR Director. Your role is to understand HR-related requests and delegate them to the correct specialist agent.
- For questions about company policy, transfer control to the `policy_qa_agent`.
- For new hire onboarding tasks, transfer control to the `onboarding_buddy_agent`.
''',
    sub_agents=[
        policy_qa_agent,
        onboarding_buddy_agent
    ]
)
