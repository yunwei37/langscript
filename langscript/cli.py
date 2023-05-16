"""CLI interface for langscript project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import argparse
import langscript.agent as agent


def main():
    """
    The main function executes on commands:
    `python -m langscript` and `$ langscript `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(description="Langscript Interpreter")
    parser.add_argument("filename", nargs="?",
                        help="Langscript file to execute")
    parser.add_argument("--version", action="version",
                        version="Langscript 1.0")

    args = parser.parse_args()

    if args.filename:
        with open(args.filename, "r") as file:
            code = file.read()
        agent.run(code)
    else:
        while True:
            user_input = input(">>> ")
            if user_input == "exit":
                break
            agent.run(user_input)
