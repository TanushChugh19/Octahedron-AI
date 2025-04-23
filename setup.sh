#!/bin/bash

# Set repository URL
REPO_URL="https://github.com/TanushChugh19/Octahedron-AI.git"
FOLDER_NAME="Octahedron-AI"

# Clone the repository
echo "Cloning the repository..."
git clone $REPO_URL
cd $FOLDER_NAME || exit

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Completion message
echo "Setup complete! You can now run the bot."
