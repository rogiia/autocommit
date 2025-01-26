# Commit Helper

## Overview

Commit Helper is a utility that assists in generating commit messages based on the changes made in your repository. It reads the git diff from standard input, processes it using a language model, and generates a commit message that follows the formatting rules defined by commitlint.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Set up a virtual environment and install dependencies:
    ```sh
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Make the script executable:
    ```sh
    chmod +x commit
    ```

4. Add the script to your PATH by updating your shell configuration file (e.g., `.bashrc`, `.zshrc`):
    ```sh
    echo 'export PATH=$PATH:/path/to/your/repository' >> ~/.bashrc
    source ~/.bashrc
    ```

## Usage

1. Make changes to your repository as usual.

2. Run the Commit Helper script:
    ```sh
    commit
    ```

3. The script will display the generated commit message and prompt you to confirm if it is acceptable:
    ```sh
    Is this commit message OK? (y/n): 
    ```

4. If you type `y`, the commit message will be used to create a commit. If you type `n`, the commit will be aborted.

## Customizing the Model

By default, the Commit Helper uses the `qwen2.5:14b` model. You can specify a different model by passing the `model_id` argument to the shell script:

```sh
commit <your-model-id>
```

## Recommended Model

Based on my experience, the smallest model that has consistently given me good results is the 14B Qwen model. It's not very fast, especially if you don't have a powerful machine, but it's better to be slow than wrong.

## License

This project is licensed under the MIT License. See the LICENSE file for details.