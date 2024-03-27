from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama

from ycrew_tools import ExtractionTools, DataFetchingTools, ChartingTools, MarkdownTools
from dotenv import load_dotenv

load_dotenv() 

class FinancialResearchAgents:
    def __init__(self):
        self.Ollama = Ollama(model="openhermes")

    def markdown_report_creator(self):
        return Agent(
            role="Markdown Report Creator",
            goal=dedent(f"""Retrieve accurate data of the metrics requested for a particular symbol."""),
            backstory=dedent(f"""Expert in creating markdown reports. The best at using tools to gather data from an API. You retrieve **EVERY** metric from QuickFS when asked and never miss a single one."""),
            tools=[
                ExtractionTools.parse_string, 
                DataFetchingTools.get_metric_data_from_quickfs],
            verbose=True,
            llm=self.Ollama,
        )

    def chart_creator(self):
        return Agent(
            role="Chart Creator",
            goal=dedent(f"""Create a chart of the data provided using the tool."""),
            backstory=dedent(f"""Expert in creating charts. You are known for receiving a list of data points and meticulously creating an accurate chart. You must use the tool provided. """),
            tools=[
                ChartingTools.create_chart
            ] ,
            verbose=True,
            llm=self.Ollama,
        )

    
    def markdown_writer(self):
        return Agent(
            role="Data Report Creator",
            goal=dedent(f"""Use *.png files in same directory to add the correct syntax a markdown file."""),
            backstory=dedent(f"""Expert in writing text inside a markdown file. You take a text input and write the contents to a markdown file in the same directory. You always add a new line after inserting into the markdown file. **YOU USE MARKDOWN SYNTAX AT ALL TIMES NO MATTER WHAT** YOU NEVER INSERT ANYTHING INTO THE report.md FILE THAT ISN'T MARKDOWN SYNTAX. """),
            tools=[MarkdownTools.write_text_to_markdown_file],
            verbose=True,
            llm=self.Ollama,
        )



     