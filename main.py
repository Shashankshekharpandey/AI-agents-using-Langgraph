import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from typing import Annotated
from langgraph.graph import MessagesState
from langgraph.graph.message import add_messages
from langchain_core.messages.ai import AIMessage

# Load API keys from .env file
load_dotenv()

# Get API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Ensure API keys are set
if not GROQ_API_KEY or not OPENAI_API_KEY or not TAVILY_API_KEY:
    raise ValueError("One or more API keys are missing. Check your .env file.")

# Initialize LLMs with API keys
openai_llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
groq_llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=GROQ_API_KEY)

# Initialize search tool
search_tool = TavilySearchResults(max_results=2, tavily_api_key=TAVILY_API_KEY)

# Define state
# class AgentState(MessagesState):
#     messages: Annotated[list, add_messages]

# Define system prompt
system_prompt = "Act as an AI chatbot who is smart and friendly"

# def process_query(state: AgentState):
#     """Function to process user query and return updated state."""
#     messages = state.get("messages", [])
#     response = groq_llm.invoke(messages[-1]["content"])
#     messages.append({"role": "assistant", "content": response})
#     return {"messages": messages}

# Create agent

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]