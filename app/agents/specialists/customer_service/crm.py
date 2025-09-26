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
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

search_crm_customer_data = VertexAiRagRetrieval(
    name='search_crm_customer_data',
    description='Searches the CRM for specific customer data, like client names, contact info, and project status.',
    rag_resources=[
        rag.RagResource(
            rag_corpus="projects/609773120808/locations/us-east4/ragCorpora/6838716034162098176"
        )
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

crm_agent = Agent(
    model='gemini-2.5-flash',
    name='crm_agent',
    description='Handles questions about CRM data and specific customers.',
    instruction='You are an expert on TradieAI\'s CRM data. Use your tool to answer questions about specific customers and their data.',
    tools=[search_crm_customer_data],
)
