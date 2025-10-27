from langchain_community.utilities import SQLDatabase
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline
from dataclasses import dataclass
from langchain_core.tools import tool
from langgraph.runtime import get_runtime
from langchain.agents import create_agent
from IPython.display import Image, display




db = SQLDatabase.from_uri("sqlite:///Chinook.db")

@dataclass
class RuntimeContext:
    db:SQLDatabase

@tool
def execute_sql(query: str) -> str:

    """Excute a SQLite command and return the result"""
    runtime = get_runtime(RuntimeContext)
    db = runtime.context.db

    try:
        return db.run(query)
    except Exception as e:
        return f"Error: {e}"
    


hf_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=150,
    temperature=0.7,
    device_map="cpu"
)
llm_pipeline = HuggingFacePipeline(pipeline=hf_pipeline)
llm = HuggingFacePipeline(pipeline=hf_pipeline)
    

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
    model=llm,
    tools= [execute_sql],
    system_prompt=SYSTEM_PROMPT,
    context_schema=RuntimeContext,
)


question = "Which table has the largest number of entries?"

for step in agent.stream(
    {"messages":question },
    context=RuntimeContext(db=db),
    stream_mode='values',

):
    step['messages'][-1].pretty_print()



# import langchain
# print(langchain.__version__)