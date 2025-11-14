from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

messages = [
    (
        "system",
        "You are a helpful assistant that suggests programming languages based on user preferences.",
    ),
    ("human", "I love Data Science and Machine Learning. Which programming language should I learn?"),
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)
