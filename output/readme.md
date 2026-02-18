# Documentation_generator_agent

The Documentation Generator Agent is a tool for generating documentation from a repository's file structure and important files.

**Project Structure**
```
README.md
LICENSE
client.py
output/
readme.md
prompts/
documentation_generator.yaml
file_selector.yaml
requirements.txt
```

The project architecture is designed to analyze the repository structure, identify important files, and generate documentation based on those files. The workflow consists of four nodes: planner, structure analyzer, file loader, and doc generator.

**Key Modules**

* `client.py`: The main entry point for the application.
* `documentation_generator.yaml` and `file_selector.yaml`: Configuration files used by the tool to determine which files are important and how to generate documentation.
* `requirements.txt`: A list of dependencies required by the project.

**Installation**
To use this tool, you will need to install the required dependencies. You can do this by running the following command:
```
pip install -r requirements.txt
```

**Usage**

1. Clone the repository and navigate to its root directory.
2. Run `client.py` using your preferred Python runtime.

**Configuration**

No configuration is required for this tool. The important files and their contents are used as-is to generate documentation.

**Contributing**
If you'd like to contribute to this project, please submit a pull request with your changes.

**Reporting Issues**
If you encounter any issues while using this tool, please report them by creating an issue on this repository's issue tracker.