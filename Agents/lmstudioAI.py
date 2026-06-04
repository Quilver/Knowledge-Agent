from langchain_core.tools import tool          # Decorator to define custom tools
from langchain.agents import create_agent # Factory to build the agent
from langchain_core.messages import HumanMessage, SystemMessage # Wrapper for user input   
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Dict, Any, Optional
from langchain_openai import ChatOpenAI,OpenAIEmbeddings  # OpenAI-compatible client for LM Studio

def llm_model():
    MODEL_ID:str = "gemma-4-e4b-it"
    llm_model = ChatOpenAI(
        model=MODEL_ID,  # ⚠️ Replace with your loaded model's name
        base_url="http://localhost:1234/v1",             # Default LM Studio API endpoint
        api_key="not-needed",                             # Placeholder key # type: ignore
        temperature=0.0                                  # Zero temperature for reliable math
    )
    return llm_model

def agent(tools, system_message):
    llm = llm_model()
    agent = create_agent(llm, tools=tools, system_prompt =system_message)
    return agent