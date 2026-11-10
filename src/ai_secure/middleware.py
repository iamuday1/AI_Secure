import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import SystemMessage, HumanMessage
load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent = create_agent(
   model="gpt-4o-mini",
   checkpointer=InMemorySaver(),
   middleware=[SummarizationMiddleware(
       model="gpt-4o-mini",
       trigger=("messages", 10),
       keep=("messages", 4)
   )],
)

config = {"configurable": {"thread_id": "test-1"}}

questions = [
    "what is 2+2?",
    "what is 10*5?",
    "what is 100/4?",
    "what is 50-20?",
    "what is 3^3?",
    "what is 4*4?"
]

for q in questions:
    response = agent.invoke(
        {"messages": [HumanMessage(content=q)]},
        config=config
    )
    print(f"Messages: {response}")
    print(f"Response: {len(response['messages'])}")