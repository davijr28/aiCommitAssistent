import typer
from git_utils import get_git_diff
from llm import generate_commit

# Creates Typer app instance
app = typer.Typer()

# Command to generate the commit message
@app.command()
def commit():
    diff = get_git_diff()
    if not diff.strip():
        print("No staged changes found. Use 'git add' first.")
        return
    
    message = generate_commit(diff)
    print(f"\nSuggested commit:\n{message}")

if __name__ == "__main__":
    app()