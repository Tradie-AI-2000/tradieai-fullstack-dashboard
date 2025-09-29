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

from app.agents.specialists.finance import (
    invoice_creator_agent,
)

Finance_Director_Agent = LlmAgent(
    name="Finance_Director_Agent",
    model="gemini-2.5-pro",
    description="Manages all finance-related tasks, such as invoicing.",
    instruction='''You are the Finance Director. Your role is to understand finance-related requests and delegate them to the correct specialist agent.
- For creating invoices, transfer control to the `invoice_creator_agent`.
''',
    sub_agents=[
        invoice_creator_agent
    ]
)
