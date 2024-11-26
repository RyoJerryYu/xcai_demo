#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install poetry
pip install poetry

# Initialize a new poetry project
poetry init --no-interaction

# Install dependencies
poetry install
