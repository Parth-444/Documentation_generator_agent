# Documentation_generator_agent
## Project Overview

The Documentation_generator_agent is a codebase analysis engine that analyzes a project structure JSON and selects files that are important for documentation generation. The system must follow specific rules to output valid JSON, exclude unnecessary files, and include only relevant files.

## Architecture / Folder Structure

The repository contains the following important files:
* `client.py`: The main script that runs the codebase analysis engine.
* `prompts/file_selector.yaml`: A YAML file that defines the system prompts for selecting important files.
* `requirements.txt`: A list of dependencies required to run the project.

## Key Modules

### `planner_node`
This module takes the repo name as input and gets the repo tree from the MCP server. It then uses this information to plan the documentation generation workflow.

### `structure_analyzer_node`
This module analyzes the repo structure to determine which files are important for documentation generation. It uses the system prompts to select relevant files.

### `file_loader_node`
This module loads the important files into chunks based on their content and size.

## Installation

To run this project, you will need to install the dependencies listed in `requirements.txt`. You can do this using pip:
```
pip install -r requirements.txt
```
## Usage

Run the main script, `client.py`, with the required inputs (e.g., repo name) to generate the documentation.

## Configuration

Not specified in repository.

## Contributing

If you would like to contribute to this project, please reach out to the maintainers or create an issue on GitHub.

## Reporting Issues

To report any issues or bugs, please submit a new issue on GitHub.
