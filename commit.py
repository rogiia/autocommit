import sys
import argparse
from llama_index.llms.ollama import Ollama
from llama_index.core.program import LLMTextCompletionProgram
from pydantic import BaseModel

class Commit(BaseModel):
    """Data model for a commit."""
    commit_message: str

def read_git_diff():
    diff = sys.stdin.read()
    return diff

def generate_commit_message(diff, model_id):
    llm = Ollama(model=model_id, request_timeout=60.0, temperature=0.1)
    prompt = """Write a commit message. The commit message should follow the formatting rules defined by commitlint. Base your commit message using the diff from the changes made in the repository.

<commitlint>
module.exports = {
  'extends': ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      ['build', 'chore', 'ci', 'docs', 'feat', 'fix', 'perf', 'refactor', 'revert', 'style', 'test']
    ],
    'scope-min-length': [2, 'always', 6],
    'subject-min-length': [2, 'always', 10],
    'body-empty': [2, 'never'],
    'body-min-length': [2, 'always', 20],
    'body-leading-blank': [2, 'always'],
    'footer-leading-blank': [2, 'always']
  }
};
</commitlint>
<example>
feat(config): change deployment config
1- Upgrade instance escalation from maximum 5 instances to 10
2- Have a minimum of 2 instances always running
</example>

<diff>
{diff}
</diff>
"""
    program = LLMTextCompletionProgram.from_defaults(
        llm=llm,
        output_cls=Commit,
        prompt_template_str=prompt
    )
    response = program(diff=diff)
    return response.commit_message

def main():
    parser = argparse.ArgumentParser(description="Read a git diff from standard input and generate a commit message.")
    parser.add_argument('--model_id', type=str, default="qwen2.5:14b", help="The model ID to use for generating the commit message.")
    args = parser.parse_args()
    
    diff = read_git_diff()
    commit_message = generate_commit_message(diff, args.model_id)
    print(commit_message)

if __name__ == "__main__":
    main()
