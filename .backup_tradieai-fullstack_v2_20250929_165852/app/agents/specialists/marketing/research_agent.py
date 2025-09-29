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

import datetime
from collections.abc import AsyncGenerator

from google.adk.agents import BaseAgent, LlmAgent, LoopAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions
from google.adk.planners import BuiltInPlanner
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.genai import types as genai_types

from app.config import config
from app.agents.specialists.marketing.research_agent_entities import Feedback

# This is a placeholder for the original callbacks. In a real scenario, you would move them to a separate file.
def collect_research_sources_callback(callback_context: CallbackContext) -> None:
    pass

def citation_replacement_callback(callback_context: CallbackContext) -> genai_types.Content:
    return genai_types.Content()

class EscalationChecker(BaseAgent):
    """Checks research evaluation and escalates to stop the loop if grade is 'pass'."""

    def __init__(self, name: str):
        super().__init__(name=name)

    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        evaluation_result = ctx.session.state.get("research_evaluation")
        if evaluation_result and evaluation_result.get("grade") == "pass":
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name)

plan_generator = LlmAgent(
    model=config.worker_model,
    name="plan_generator",
    description="Generates or refines a multi-step research plan.",
    tools=[google_search],
)

research_pipeline = SequentialAgent(
    name="research_pipeline",
    description="Executes a research plan, including web searches, analysis, and final report composition.",
    sub_agents=[
        LlmAgent(
            model=config.worker_model,
            name="section_planner",
            instruction="You are an expert report architect...",
            output_key="report_sections",
        ),
        LlmAgent(
            model=config.worker_model,
            name="section_researcher",
            instruction="You are a highly capable research and synthesis agent...",
            tools=[google_search],
            output_key="section_research_findings",
            after_agent_callback=collect_research_sources_callback,
        ),
        LoopAgent(
            name="iterative_refinement_loop",
            max_iterations=config.max_search_iterations,
            sub_agents=[
                LlmAgent(
                    model=config.critic_model,
                    name="research_evaluator",
                    instruction="You are a meticulous quality assurance analyst...",
                    output_schema=Feedback,
                    output_key="research_evaluation",
                ),
                EscalationChecker(name="escalation_checker"),
                LlmAgent(
                    model=config.worker_model,
                    name="enhanced_search_executor",
                    instruction="You are a specialist researcher executing a refinement pass...",
                    tools=[google_search],
                    output_key="section_research_findings",
                    after_agent_callback=collect_research_sources_callback,
                ),
            ],
        ),
        LlmAgent(
            model=config.critic_model,
            name="report_composer_with_citations",
            instruction="Transform the provided data into a polished, professional, and meticulously cited research report...",
            output_key="final_cited_report",
            after_agent_callback=citation_replacement_callback,
        ),
    ],
)

research_agent = LlmAgent(
    name="research_agent",
    model=config.worker_model,
    description="A specialist agent that performs deep, multi-step research on a given topic and returns a comprehensive report.",
    instruction=f"""
    You are a specialist research agent, activated by your director to handle a research task.
    Your job is to use a research pipeline to generate a comprehensive report.
    """,
    sub_agents=[
        research_pipeline
    ]
)
