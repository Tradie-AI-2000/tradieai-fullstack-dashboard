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

import csv

from google.adk.agents import LlmAgent


def get_expense_report(quarter: str) -> str:
    """Reads the expenses.csv file and generates a summary for a given quarter."""
    quarter_map = {
        "Q1": ["01", "02", "03"],
        "Q2": ["04", "05", "06"],
        "Q3": ["07", "08", "09"],
        "Q4": ["10", "11", "12"],
    }
    months_in_quarter = quarter_map.get(quarter.upper())
    if not months_in_quarter:
        return f"Invalid quarter: {quarter}. Please specify Q1, Q2, Q3, or Q4."

    try:
        total_expense = 0.0
        category_expenses = {}
        with open("expenses.csv", mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date_month = row["Date"].split('-')[1]
                if date_month in months_in_quarter:
                    amount = float(row["Amount"])
                    category = row["Category"]
                    total_expense += amount
                    category_expenses[category] = category_expenses.get(category, 0) + amount

        if total_expense == 0:
            return f"No expenses found for {quarter}."

        report = f"""--- Expense Report for {quarter} ---
Total Expenses: ${total_expense:,.2f}

Expenses by Category:"""
        for category, amount in sorted(category_expenses.items(), key=lambda item: item[1], reverse=True):
            report += f"\n- {category}: ${amount:,.2f}"

        return report

    except FileNotFoundError:
        return "Error: The expenses.csv file was not found."
    except Exception as e:
        return f"An error occurred while generating the expense report: {e}"

expense_reporter_agent = LlmAgent(
    name="expense_reporter_agent",
    model="gemini-2.5-flash",
    description="Use this agent to get a summary report of business expenses for a specific quarter.",
    instruction="Use the `get_expense_report` tool to fetch the expense report for the requested quarter.",
    tools=[get_expense_report]
)
