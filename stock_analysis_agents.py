import os
from crewai import Agent
from langchain_community.llms import Ollama

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools

from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool

# spin up a local LLM
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] ='openhermes'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] =''
mistral = Ollama(model="openhermes")

class StockAnalysisAgents():
    def financial_analyst(self):
        return Agent(
            role='The Best Financial Analyst',
            goal="""Impress all customers with your financial data 
            and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
            lots of expertise in stock market analysis and investment
            strategies that is working for a super important customer.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k
            ],
            llm=mistral
        )

    def research_analyst(self):
        return Agent(
            role='Staff Research Analyst',
            goal="""Being the best at gather, interpret data and amaze
            your customer with it""",
            backstory="""Known as the BEST research analyst, you're
            skilled in sifting through news, company announcements, 
            and market sentiments. Now you're working on a super 
            important customer""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool(),
                SECTools.search_10q,
                SECTools.search_10k
            ],
            llm=mistral
    )

    def investment_advisor(self):
        return Agent(
            role='Private Investment Advisor',
            goal="""Impress your customers with full analyses over stocks
            and complete investment recommendations""",
            backstory="""You're the most experienced investment advisor
            and you combine various analytical insights to formulate
            strategic investment advice. You are now working for
            a super important customer you need to impress.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool()
            ],
            llm=mistral
    )