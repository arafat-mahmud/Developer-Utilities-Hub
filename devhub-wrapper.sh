#!/bin/bash

# DevHub Wrapper Script
# This script activates the DevHub environment and runs commands

DEVHUB_DIR="/Users/sanon/Developer-Utilities-Hub"

# Check if DevHub directory exists
if [ ! -d "$DEVHUB_DIR" ]; then
    echo "❌ Error: DevHub not found at $DEVHUB_DIR"
    echo "Please make sure DevHub is installed correctly."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "$DEVHUB_DIR/devhub-env" ]; then
    echo "❌ Error: DevHub virtual environment not found"
    echo "Please run the installation script first:"
    echo "cd $DEVHUB_DIR && ./install.sh"
    exit 1
fi

# Activate virtual environment and run DevHub
cd "$DEVHUB_DIR"
source devhub-env/bin/activate
devhub "$@"
