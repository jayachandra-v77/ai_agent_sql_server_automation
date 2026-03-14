import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse


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

sql_agent = create_sql_agent(
    llm = llm,
    db=db,
    verbose=False
)



# FastAPI
app = FastAPI()

class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(q: Question):
    try:
        response = sql_agent.invoke(q.question)
        return {"answer": response["output"]}
    except Exception as e:
        return {"error": str(e)}
    

# Serve index.html from root
@app.get("/")
def get_index():
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(index_path)