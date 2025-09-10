import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

# Set Groq API Key (make sure it's in your .env file as GROQ_API_KEY)
groq_api_key = os.getenv("GROQ_API_KEY")

config_list = [{
    "model": "llama-3.3-70b-versatile",
    "api_key": groq_api_key,
    "api_type": "groq"
}]

assistant = AssistantAgent(
    name="groq_agent",
    system_message="You are a helpful assistant.",
    llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)

# Groq doesn't have a direct serpapi tool integration yet,
# so you could implement serpapi as a custom tool or handle externally.
# Here we just demonstrate running a question query like your example.

query = "what was the GDP of INDIA in 2024 plus 5 ?"

result = user_proxy.initiate_chat(
    assistant,
    message=query
)

print(result)
