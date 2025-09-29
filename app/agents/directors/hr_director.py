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

HR_Director_Agent = LlmAgent(
    name="HR_Director_Agent",
    model="gemini-2.5-pro",
    description="Manages Human Resources tasks.",
    instruction='''You are the HR Director. You can no longer answer questions about company policy or employee onboarding.
Please inform the user that these capabilities are currently unavailable.
''',
    sub_agents=[]
)
