**Project Title:** Documentation_generator_agent

**Overview:**
This repository contains an agent for generating documentation based on a given project structure.

**Architecture / Folder Structure:**

The repository consists of several key files and folders:
- `client.py`: The main application file that runs the documentation generation process.
- `output`: A folder containing generated documentation files, including this README.md file.
- `prompts`: A folder containing YAML configuration files for the documentation generator.

**Key Modules:**
- `planner_node`: Initializes the documentation generation process by planning the node structure.
- `structure_analyzer_node`: Analyzes the project structure and extracts important files.
- `file_loader_node`: Loads important files into chunks, splitting them if necessary.
- `doc_generator_node`: Generates documentation based on the loaded file chunks.

**Installation:**
Not specified in repository. Please refer to individual package installation instructions or a CI/CD pipeline setup.

**Usage:**
The agent can be run as a standalone application using the `client.py` script. The output will include generated documentation files in the `output` folder.

**Configuration:**
The agent is configured through YAML files in the `prompts` folder, specifically:
- `documentation_generator.yaml`: Defines the project structure and important files.
- `file_selector.yaml`: Selects which files are important for generating documentation.

**Contributing:**
This repository accepts contributions to improve its functionality, maintainability, or readability. Please create an issue or pull request to discuss your ideas.

**Reporting Issues:**
If you encounter any issues while using the agent, please report them on this repository's issue tracker.
