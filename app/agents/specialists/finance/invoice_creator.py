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
import os

from google.adk.agents import LlmAgent


def create_invoice(customer_name: str, amount: float) -> str:
    """Creates a detailed invoice and saves it to a file."""
    invoice_id = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{abs(hash(customer_name)) % 10000:04d}"
    invoice_date = datetime.datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join("invoices", f"invoice_{invoice_id}.txt")

    content = (
        f"--- INVOICE ---\n\n"
        f"Invoice ID: {invoice_id}\n"
        f"Date: {invoice_date}\n\n"
        f"Bill To:\n"
        f"{customer_name}\n\n"
        f"--------------------\n"
        f"Description         Amount\n"
        f"--------------------\n"
        f"Consulting Services   ${amount:,.2f}\n"
        f"--------------------\n"
        f"TOTAL:              ${amount:,.2f}\n"
    )

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully created invoice. It is saved at: {file_path}"
    except IOError as e:
        return f"Error: Failed to save invoice to {file_path}. Reason: {e}"

invoice_creator_agent = LlmAgent(
    name="invoice_creator_agent",
    model="gemini-2.5-flash",
    description="Use this agent to create a new invoice for a customer.",
    instruction="Use the `create_invoice` tool to generate an invoice for the specified customer and amount.",
    tools=[create_invoice]
)
