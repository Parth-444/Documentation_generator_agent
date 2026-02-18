# Documentation_generator_agent
Overview
--------

The Documentation Generator Agent is a system designed to generate documentation for GitHub repositories based on their structure and important files. It uses various components, including LangGraph, MCP, and LLM (Large Language Model), to analyze the repository's file structure and content, identify key modules and files, and generate documentation in markdown format.

Architecture / Folder Structure
------------------------------

The system consists of several folders and files:

*   `client.py`: The main entry point for the system, responsible for initializing the workflow and invoking the various nodes.
*   `prompts/` directory: Contains YAML files defining prompts for the LLM to use in generating documentation. Specifically:
    +   `file_selector.yaml`: Defines a prompt to select important files from the repository.
    +   `documentation_generator.yaml`: Defines a prompt to generate documentation based on the selected files and their contents.
*   `output/` directory: Contains the generated documentation in markdown format.

Key Modules
-------------

The system has several key modules:

1.  **Planner Node**: Analyzes the repository's file structure and identifies important files.
2.  **Structure Analyzer Node**: Analyzes the selected files' contents to determine their relevance to the documentation.
3.  **File Loader Node**: Loads the identified files into chunks for processing.
4.  **Documentation Generator Node**: Generates documentation based on the processed file contents.

Installation
------------

To use this system, follow these steps:

1.  Clone the repository: `git clone https://github.com/Parth-444/Documentation_generator_agent.git`
2.  Install dependencies: `pip install -r requirements.txt`

Usage
-----

Run the main entry point: `python client.py`