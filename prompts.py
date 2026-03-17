PROMPT = """
You are a tool that writes Conventional Commit messages.

Rules:
- Use conventional commit format
- Be concise
- Use types like feat, fix, refactor, docs, test, chore

Git diff:

{diff}

Generate only the commit message.
"""