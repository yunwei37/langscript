"""
langscript base module.

This is the principal module of the langscript project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

# example constant variable
NAME = "langscript"


def run(code: str):
    """Run a piece of code.

    Args:
        code (str): The code to run.
    """
    print(f"Running code: {code}")
    # First, let's load the language model we're going to use to control the agent.
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo", client=None)
    # Next, let's load some tools to use.
    # Note that the `llm-math` tool uses an LLM, so we need to pass that in.
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    # Finally, let's initialize an agent with the tools, the language model,
    # and the type of agent we want to use.
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    # Now let's test it out!
    agent.run(code)
