import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage
from typing import Sequence, Literal


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found in .env")
    st.stop()


class State(TypedDict):
    messages: Sequence[BaseMessage]



def ask_question(state: State) -> State:
    # Just return state; Streamlit handles UI question
    return state


def chatbot(state: State) -> State:
    response = chat.invoke(state["messages"])
    return State(messages=[response])


def ask_another_question(state: State) -> State:
    return state


def routing_function(state: State) -> Literal["ask_question", "__end__"]:
    user_answer = state["messages"][0].content.lower()
    if user_answer.strip() == "yes":
        return "ask_question"
    return "__end__"



chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)



graph = StateGraph(State)

graph.add_node("ask_question", ask_question)
graph.add_node("chatbot", chatbot)
graph.add_node("ask_another_question", ask_another_question)

graph.add_edge(START, "ask_question")
graph.add_edge("ask_question", "chatbot")
graph.add_edge("chatbot", "ask_another_question")

graph.add_conditional_edges(
    source="ask_another_question", 
    path=routing_function
)

graph_compiled = graph.compile()


st.title("🤖 LangGraph Chatbot Simulator (Streamlit) by Jasman")



if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "step" not in st.session_state:
    st.session_state.step = "ask_question"



for msg in st.session_state.conversation:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Type your message...")

if user_input:
  
    st.session_state.conversation.append({"role": "user", "content": user_input})

    state = State(messages=[HumanMessage(user_input)])

    result = None
    if st.session_state.step == "ask_question":
        result = graph_compiled.invoke(state)
        st.session_state.step = "ask_another_question"

    elif st.session_state.step == "ask_another_question":
        result = graph_compiled.invoke(state)
        if user_input.lower() == "yes":
            st.session_state.step = "ask_question"
        else:
            st.session_state.step = "__end__"


    if result and result["messages"]:
        ai_msg = result["messages"][0].content
        st.session_state.conversation.append({"role": "assistant", "content": ai_msg})

        with st.chat_message("assistant"):
            st.write(ai_msg)

    if st.session_state.step == "__end__":
        st.session_state.conversation.append(
            {"role": "assistant", "content": "Thank you! Chat ended."}
        )
        st.experimental_rerun()
