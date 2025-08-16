# DevHub Docker Image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js for JavaScript/TypeScript formatting
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g prettier

# Install Go for Go formatting
RUN curl -L https://go.dev/dl/go1.21.0.linux-amd64.tar.gz | tar -C /usr/local -xzf - \
    && ln -s /usr/local/go/bin/* /usr/local/bin/

# Install Rust for Rust formatting
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && . ~/.cargo/env \
    && rustup component add rustfmt

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml README.md LICENSE ./
COPY src/ ./src/

# Install DevHub
RUN pip install -e .

# Create workspace directory
RUN mkdir -p /workspace
WORKDIR /workspace

# Set up entrypoint
ENTRYPOINT ["devhub"]
CMD ["--help"]

# Labels
LABEL maintainer="DevHub Team <hello@devhub.dev>"
LABEL description="The Swiss Army Knife for Developers"
LABEL version="1.0.0"
