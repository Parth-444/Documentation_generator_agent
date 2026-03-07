# Documentation_generator_agent

## Overview

The `Documentation_generator_agent` is an automated system designed to generate professional `README.md` documentation for GitHub repositories. It addresses the challenge of manually creating comprehensive documentation by leveraging an intelligent, multi-step AI agent pipeline built with LangGraph.

The system operates by first taking a repository name as input. It then interacts with a GitHub server via a Multi-Server Client Protocol (MCP) to obtain the repository's file tree. A Large Language Model (LLM) subsequently analyzes this structure to identify files critical for documentation. The content of these important files is then loaded, chunked, and fed into another LLM, which synthesizes a comprehensive `README.md` based on predefined prompts and the extracted repository context. This end-to-end workflow automates the documentation process, providing a structured and context-aware output.

## Architecture / Folder Structure

```
.
├── LICENSE
├── README.md
├── client.py
├── output/
│   └── readme.md
├── prompts/
│   ├── documentation_generator.yaml
│   └── file_selector.yaml
└── requirements.txt
```

The project is structured around `client.py`, which orchestrates the documentation generation workflow. Configuration for the LLM prompts is stored in the `prompts/` directory, and the generated documentation is saved in `output/`. This modular design separates the core logic from configuration and output.

## Key Modules

*   `client.py`: The main entry point of the system, which coordinates the workflow and runs the different nodes of the LangGraph agent. It initializes the LLM, MCP client, and defines the agent's state and workflow.
*   `planner_node`: The initial node in the agent pipeline. It takes the repository name and retrieves the repository tree from the GitHub MCP server, setting up the context for subsequent analysis.
*   `structure_analyzer_node`: Receives the repository structure from the `planner_node`. It utilizes an LLM, guided by the `file_selector.yaml` prompt, to analyze the tree and identify which files are most important for generating comprehensive documentation.
*   `file_loader_node`: Takes the paths of the identified important files. It fetches their content from the GitHub MCP server and then splits the content into manageable chunks using `RecursiveCharacterTextSplitter` for efficient processing by the documentation generator.
*   `doc_generator_node`: The final node responsible for generating the documentation. It aggregates the loaded file chunks, uses an LLM (guided by the `documentation_generator.yaml` prompt) to synthesize a professional `README.md`, and incorporates other repository metadata like the username.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Parth-444/Documentation_generator_agent.git
    cd Documentation_generator_agent
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ensure your Ollama server is running and the `llama3:8B` model is available.
4.  Ensure the MCP GitHub server is configured and accessible as specified in `client.py`.

## Usage

The system can be run from the command line by executing the main client script. This will initiate the documentation generation process for the specified repository.

```bash
python client.py
```

Upon successful execution, the generated documentation will be saved to the `output/readme.md` file within the repository.

## External Dependencies

*   **LangGraph**: A library used for building stateful, multi-actor applications with LLMs. It defines and manages the agent's workflow, orchestrating the sequence of nodes for planning, analysis, loading, and documentation generation.
*   **Ollama**: An open-source framework for running Large Language Models locally. It provides the `llama3:8B` model, which is utilized for both intelligently selecting important files and generating the final Markdown documentation.
*   **MCP (MultiServerMCPClient)**: A multi-server client library that enables the system to interact with external services concurrently. In this project, it is configured to communicate with a `github_server` to retrieve repository trees, file contents, and user information necessary for documentation.

## Configuration

The system's behavior, particularly regarding LLM interactions, can be configured by modifying the YAML files located in the `prompts` directory:

*   `documentation_generator.yaml`: Defines the system and user prompts used by the `doc_generator_node` to guide the LLM in generating the final `README.md` content.
*   `file_selector.yaml`: Defines the system and user prompts used by the `structure_analyzer_node` to instruct the LLM on how to identify and select important files from the repository structure.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Reporting Issues

Not specified in repository