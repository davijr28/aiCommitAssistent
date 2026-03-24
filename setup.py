from setuptools import setup

setup(
    name="aiCommitAssistent",
    version="1.0",
    py_modules=["main", "git_utils", "llm", "help", "prompts"],
    install_requires=[
        "typer",
        "rich",
        "pycountry",
        "python-dotenv",
        "google-genai",
    ],
    entry_points={
        "console_scripts": [
            "aicm = main:app",
        ],
    },
)
