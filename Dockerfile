FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files first for better caching
COPY pyproject.toml uv.lock ./

# Copy source code
COPY src/ ./src/
COPY __init__.py ./

# Copy .env file
COPY .env ./

# Expose port if your server uses one (adjust as needed)
EXPOSE 9999

# Run the server
CMD ["uv", "run", "src/server/server.py"]