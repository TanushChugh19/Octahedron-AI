#!/bin/bash

# Copyright (c) 2025 Tanush Chugh
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

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
