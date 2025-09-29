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

search_company_information = VertexAiRagRetrieval(
    name='search_company_information',
    description='Searches for general company information about TradieAI, including its services, contact details, and "about us" pages.',
    rag_resources=[
        rag.RagResource(
            rag_corpus="projects/tradieai-fullstack-production/locations/us-east4/ragCorpora/3379951520341557248"
        )
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

company_info_agent = Agent(
    model='gemini-2.5-flash',
    name='company_info_agent',
    description='Handles questions about general company information, services, and contact details.',
    instruction='You are an expert on TradieAI company information. Use your tool to answer questions about services, contact details, and "about us" information.',
    tools=[search_company_information],
)
