from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class StockAnalysisCrew:
    def __init__(self, companyName):
        self.companyName = companyName

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        financial_analyst_agent = agents.financial_analyst()
        investment_advisor_agent = agents.investment_advisor()

        print(f"Researching {self.companyName}...")
        research_task = tasks.research(research_analyst_agent, self.companyName)
        financial_task = tasks.financial_analysis(financial_analyst_agent)
        filings_task = tasks.filings_analysis(financial_analyst_agent)
        recommend_task = tasks.recommend(investment_advisor_agent)

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent
            ],
            tasks=[
                research_task,
                financial_task,
                filings_task,
                recommend_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("--   Stock Analysis Crew  --")
    print("----------------------------")
    companyName = input(
        dedent("""
            What company do you want to analyze?
               """))
    stock_analysis_crew = StockAnalysisCrew(companyName)
    result = stock_analysis_crew.run()
    print("------------- Report below ---------------")
    print(result)
    print("------------------------------------------")



       
