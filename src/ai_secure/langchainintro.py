import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# def get_weather(city):
#     """Get the current weather for a given city."""
#     # Placeholder function to simulate fetching weather data
#     return f"The current weather in {city} is sunny with a temperature of 25°C."

# agent = create_agent(
#    model="gpt-5",
#    tools=[get_weather],
#    system_prompt="You are a helpful assistant."
# )

# response = agent.invoke({"messages": [{"role": "user", "content": "What's the weather like in New York?"}]})

# print(response["messages"])

# model = init_chat_model("gpt-4.1")
# response = model.invoke("Hello, how are you?")

# model = init_chat_model("google_genai:gemini-3.5-flash-lite")
# response = model.invoke("why do parrots talk?")


model = ChatOpenAI(model_name="gpt-4.1")
# response = model.invoke("Hello, how are you?")
# print(response.content)

# for chunk in model.stream("Write me a 200 word essay on the importance of AI in modern society."):
#     print(chunk.text, end="")

# responses = model.batch([
#     "Hello, how are you?",
#     "How do airplanes fly?",
#     "What is quantum computing"],
#     config={
#         'max_concurrency': 5,
#     }
#     )

# for response in responses:
#     print(response)