from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,  RunConfig
import os
import chainlit as cl
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_api_key
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.0-flash",
)

config = RunConfig (
     model=model,
    model_provider="gemini-2.0-flash",
    tracing_disabled=True
)

web_developer:Agent = Agent(
    name="Web developer",
    instructions="You are expert in web development.",
    handoff_description="You are expert in web development.",
    model=model
)

math_tutor:Agent = Agent(
    name="math tutor",
    instructions="You are mathematics teacher.",
    handoff_description="You are mathematics teacher.",
    model=model
)


science_tutor:Agent = Agent(
    name="science tutor",
    instructions="You are science teacher.",
    handoff_description="You are science teacher.",
    model=model
)

english_tutor:Agent = Agent(
    name="english tutor",
    instructions="You are english teacher.",
    handoff_description="You are english teacher.",
    model=model
)

triage = Agent(
    name="Triage Agent",
    instructions="You will decide which agent to use based on user's task. And also mention the name of agent that has completed the given task.",
    handoffs=[web_developer,math_tutor,science_tutor,english_tutor],
    model=model
    
    )

@cl.on_message
async def main(message:cl.Message):

    result = await Runner.run(
       triage,input=message.content, run_config=config
       
    )

    await cl.Message(
        content=result.final_output
    ).send()


