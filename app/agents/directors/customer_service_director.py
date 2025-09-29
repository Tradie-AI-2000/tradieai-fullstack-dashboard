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

Customer_Service_Director_Agent = Agent(
    model='gemini-2.5-pro',
    name='Customer_Service_Director_Agent',
    description="Manages customer service inquiries.",
    instruction="""
        You are a customer service agent. You can no longer answer questions about general company information or specific CRM data.
        Please inform the user that these capabilities are currently unavailable.
    """,
    sub_agents=[]
)
