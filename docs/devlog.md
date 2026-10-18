# Devlog Learntopia

## 2026-10-17 - 2026-10-19 ~ Project Initialization

This was the start of the Learntopia project. I've had the plan for a while, but now it's time to actually build it. As I don't want this to be a vibe-coding project and I had never set up a project this big before, I had to look up some best practices for getting started.
I ended up with ruff for linting and formatting, mypy for static type checking and pre-commit to run both automatically before every commit.
I also wrote my first unit test in Python and GitHub workflows which aren't complex, but took a bit of research, figuring out what I could and need to do.
Since I usually don't write code without the help of AI, I was very happy about my first "passed" unit test, a working cli-command `uv run learntopia --version` and a running GitHub workflow.
Now the setup-phase is finished and I can start with the real project.