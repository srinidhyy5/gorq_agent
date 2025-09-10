import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

config_list = [{
    "model": "llama-3.3-70b-versatile",
    "api_key": os.getenv("GROQ_API_KEY"),
    "api_type": "groq"
}]

assistant = AssistantAgent(
    name="groq_agent",
    system_message="You are a helpful agent.",
    llm_config={"config_list": config_list}
)
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)
result = user_proxy.initiate_chat(
    assistant,
    message="where was elon musk born? what is his age right now in 2025?"
)
print(result)
