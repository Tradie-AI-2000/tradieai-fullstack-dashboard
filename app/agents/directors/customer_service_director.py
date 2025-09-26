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

from google.adk.agents import Agent

from app.agents.specialists.customer_service import (
    company_info_agent,
    crm_agent,
)

Customer_Service_Director_Agent = Agent(
    model='gemini-2.5-pro',
    name='Customer_Service_Director_Agent',
    description="Manages customer service inquiries, including general company questions and specific CRM data lookups.",
    instruction="""
        You are a router. Your job is to delegate the user's query to the correct specialist agent.

        - If the user asks about general company information, services, contact details, or "about us" information, delegate to the `company_info_agent`.
        - If the user asks about specific customers, clients, or CRM data, delegate to the `crm_agent`.

        Do not answer the question yourself. Only delegate to the appropriate agent.
    """,
    sub_agents=[
        company_info_agent,
        crm_agent,
    ]
)
