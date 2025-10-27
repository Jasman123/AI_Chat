from langchain_community.utilities import SQLDatabase
from dataclasses import dataclass
from langchain_core.tools import tool
from langgraph.runtime import get_runtime
from langchain.agents import create_agent


db = SQLDatabase.from_uri("sqlite:///Chinook.db")

@dataclass
class RuntimeContext:
    db:SQLDatabase

@tool
def excute_sql(query:str) ->str:
    """Excute a SQLite command and return the result"""
    runtime = get_runtime(RuntimeContext)
    db = runtime.context.db

    try:
        return db.run(query)
    except Exception as e:
        return f"Error: {e}"
    

SYSTEM_PROMPT = """You are a careful SQlite analyst.

Rules:
- Think step-by-step.
- When you need data, call the tool 'excute_sql' with ONE SELECT query.
- Read-only only; no INSERT/UPDATE/DELETE/ALTER/DROP/CREATE/REPLACE/TRUNCATE.
- Limit to 5 rows of output unless  the use explicitly ask otherwise.
- If the tool error return 'Error:', revise the SQL and try again.
- Prefer explicit column lists, avoid SELECT *.

"""

agent = create_agent(
    model="openai:gpt-5",
    tools= [excute_sql],
    system_prompt=SYSTEM_PROMPT,
    context_schema=RuntimeContext,
)




# import langchain
# print(langchain.__version__)