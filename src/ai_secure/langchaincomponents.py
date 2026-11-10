import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

@tool
def get_weather(city):
    """Get the current weather for a given city."""
    # Placeholder function to simulate fetching weather data
    return f"The current weather in {city} is sunny with a temperature of 25°C."

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

model_with_tools = model.bind_tools([get_weather])


# response = model_with_tools.invoke("What's the weather like in New York?")
# print(response)
# for tool_call in response.tool_calls:
#     print(f"Tool:{tool_call['name']}")
#     print(f"Args:{tool_call['args']}")

messages = [
    {"role": "user", "content": "What's the weather like in New York?"}
    ]

ai_messages = model_with_tools.invoke(messages)

messages.append(ai_messages)

for tool_call in ai_messages.tool_calls:
    tool_result = get_weather.invoke(tool_call)
    messages.append(tool_result)

final_response = model_with_tools.invoke(messages)

print(final_response)
