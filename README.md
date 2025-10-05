# A2A Agent Project

A multi-agent system with specialized agents for different domains.

Based on [helloworld](https://github.com/a2aproject/a2a-samples/tree/main/samples/python/agents/helloworld) by google.

## Installation

This project is managed with `uv`. To install:
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install -e .

# Install dev dependencies
uv pip install -e ".[dev]"