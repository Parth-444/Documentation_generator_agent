# Documentation_generator_agent

## Overview

The `Documentation_generator_agent` is an automated system designed to streamline the creation of professional `README.md` files for software repositories. By leveraging a multi-agent pipeline built with LangGraph, it replaces manual documentation efforts with an intelligent, context-aware synthesis process.

The system works by connecting to a GitHub repository via the Multi-Server Client Protocol (MCP), extracting the directory structure, and identifying key files for analysis. An LLM-based agent pipeline then processes these files, generates meaningful summaries, and synthesizes a final documentation file. This approach ensures that documentation remains accurate and reflective of the actual codebase structure.

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

The system is architected as a sequential LangGraph workflow. It begins with a **planner** that maps the repository, followed by a **structure analyzer** that identifies essential files, a **file loader** that ingests and chunks source code, and a **documentation generator** that synthesizes the final Markdown output.

## Key Modules

*   `client.py`: The central orchestrator. It manages the LangGraph state, interacts with MCP tools to fetch repository data, and coordinates the transitions between nodes.
*   `planner_node`: Interfaces with the GitHub MCP server to retrieve the repository file tree.
*   `structure_analyzer_node`: Utilizes an LLM to evaluate the repository tree and pinpoint files critical for documentation (e.g., configurations, core logic).
*   `file_loader_node`: Fetches raw file contents, splits them into semantic chunks, and prepares them for the generation engine.
*   `doc_generator_node`: Aggregates the chunks and repository metadata to produce the final `README.md` using configured prompts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Parth-444/Documentation_generator_agent.git
   cd Documentation_generator_agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the MCP GitHub server is operational. Update `client.py` with the correct path to your local `github_mcp_server/main.py`.

4. Configure your environment:
   ```bash
   export GOOGLE_API_KEY='your-api-key-here'
   ```

## Usage

Execute the main client script to trigger the automated documentation generation:

```bash
python client.py
```

The generated documentation will be saved in `output/readme.md`.

## External Dependencies

*   **LangGraph**: Coordinates the agent state and workflow execution.
*   **ChatGoogleGenerativeAI (Gemini 2.5 Flash)**: Provides the reasoning capabilities for file selection and text synthesis.
*   **MCP (Multi-Server Client Protocol)**: Enables secure, tool-based interaction with the GitHub repository.

## Configuration

Customization is managed via the YAML files in the `prompts/` directory:

*   `documentation_generator.yaml`: Configures the system instructions and formatting rules for the final Markdown output.
*   `file_selector.yaml`: Defines the criteria used by the model to distinguish between essential project files and noise (e.g., build artifacts).

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request for any improvements or bug fixes.

## Reporting Issues

Not specified in repository
