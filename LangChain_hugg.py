from config import HUGGINGFACEHUB_API_TOKEN
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage



llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=200,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)

chat_model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You are a helpful data science assistant."),
    HumanMessage(content="Explain the difference between supervised and unsupervised learning.")
]

# Run the model
response = chat_model.invoke(messages)

print(response.content)