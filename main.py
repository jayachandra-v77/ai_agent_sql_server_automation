import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent


#load environmental variables

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
server = os.getenv("server")
database = os.getenv("database")


#creating connection

connection = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"

    
)

engine = create_engine(connection)



db = SQLDatabase(engine=engine)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)

agent = create_sql_agent(
    llm = llm,
    db=db,
    verbose=False
)


# Run query loop

while True:
    question = input("\nPlease ask your question(or type exit): ")

    if question.lower().strip() == "exit":
        print("Bye for now..!!")
        break

    try:
        response = agent.invoke(question)

        print("\nAnswer")
        print(response["output"])

    except Exception as e:
        print("\nError:", e)