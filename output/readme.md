# Documentation_generator_agent
Overview
--------

The Documentation Generator Agent is a system that generates documentation for GitHub repositories. It uses natural language processing (NLP) and machine learning (ML) techniques to analyze the repository structure, identify important files, and generate documentation in Markdown format.

Architecture / Folder Structure
-----------------------------

    README.md
    LICENSE
    client.py
    output/
        readme.md
    prompts/
        documentation_generator.yaml
        file_selector.yaml
    requirements.txt

Key Modules
------------

* `client.py`: The main entry point of the system, which coordinates the workflow and runs the different nodes.
* `planner_node`: Analyzes the repository structure to identify important files and determine the order in which they should be processed.
* `structure_analyzer_node`: Analyzes the important files to identify their contents and extract relevant information.
* `file_loader_node`: Loads the important files into chunks, which are then used by the documentation generator.
* `doc_generator_node`: Generates the documentation from the chunks using natural language processing (NLP) techniques.

Installation
------------

1. Clone the repository: `git clone https://github.com/Parth-444/Documentation_generator_agent.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the main entry point: `python client.py`

Usage
-----

The system can be run from the command line by executing `python client.py`. This will generate the documentation for the repository and save it to the `output/readme.md` file.

External Dependencies
-------------------

* LangGraph: A library for natural language processing (NLP) tasks.
* Ollama: An open-source LLaMA model for text generation.
* MCP: A multi-server client for interacting with multiple servers concurrently.

Configuration
-------------

The system can be configured by modifying the `prompts` directory, which contains YAML files that define the prompts used in the NLP tasks. The `documentation_generator.yaml` file defines the prompt used to generate documentation, while the `file_selector.yaml` file defines the prompt used to select important files.

Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.