# langscript

[![codecov](https://codecov.io/gh/yunwei37/langscript/branch/main/graph/badge.svg?token=langscript_token_here)](https://codecov.io/gh/yunwei37/langscript)
[![CI](https://github.com/yunwei37/langscript/actions/workflows/main.yml/badge.svg)](https://github.com/yunwei37/langscript/actions/workflows/main.yml)

<p align="center">
  <br>The true natural language programing script.</br>
    <br>No grammar, no syntax, no rules, no limits, Just write what you want to do in complex instructions.</br>
        <br>Take action with LLM, and have better control than AutoGPT.</br>
</p>

## examples

Hello World:

```
Say hello world to our friends to the outside world!
```

Loop:
```
Here is a sentence, "Hello World ".
I want you to add a "hello " to the end of the sentence above, and print it out. 
I want the above instructions to be executed 10 times, and you give me the output.
```

if else:
```
It was Monday the day before yesterday, you went to the supermarket and bought an apple. You have it in your hands today.

If it's Tuesday today, tell the output "yes", and ignore the following instructions.
else, read the "Disclaimer of AutoGPT", summary it in Chinese, You can call the summary "Chinese Disclaimer of AutoGPT summary".
```

Create a function or task to do something, and call it:

```
Sure! Here are the revised instructions in English:

I have a task for you called "Translate and Create Novel Chapters Based on an Outline." I will provide you with the chapter outline and background information. Your task is to:
1. Write the content of the chapter based on the outline and background information provided.
2. Translate the chapter content into English. The translation should be of high quality and exhibit excellent writing style.

Now, translate and Create Novel Chapters Based on the Outline "Chapter 1: The Beginning of the End"
```

import a module or use the specify functionality, like file system and network:

```
I want you to access my file system and network.

Now, search for the news for AI and ML，tell me the one you think is the most interesting.
translate it into Chinese and save it to "interesting.txt" in my file system.
```

A more complex example to write a Project code:

```
I have a task for you called "Write Project Code." In order to write a single module, we need to know the project's directory structure, the requirements for each module, and the overall project requirements.

When writing a module, follow these steps:
1. Perform requirement analysis to help clarify the corresponding requirements. You can write a paragraph outlining the requirements.
2. Present the written requirements to me for confirmation. Once I approve them, we can proceed to the next step.
3. Divide the project into modules and units, and further design the corresponding technical approach.
4. Based on the technical approach, build a code framework and execute the necessary commands in the command line to create a project.
5. Next, perform the task "Write Code for a Single Module" for each module.
6. Finally, once all modules have been written, conduct integration testing to ensure the overall functionality of the project.

Please note that during the process, it's important to write unit tests for each module and ensure they pass before moving on.

Now, please write code to build a website for the langscript project.
```

## Install it from PyPI

```bash
pip install langscript
```

## Usage

```py
from langscript import BaseClass
from langscript import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m langscript yourscript.ls
#or
$ langscript yourscript.ls
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.