#!/bin/bash
# Check if venv directory exists and delete it if it does
if [ -d ".venv" ]; then
    rm -rf .venv
fi

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Check if requirements.txt is not empty and install the specified dependencies
if [ -s "requirements.txt" ]; then
    pip install -r requirements.txt
else
    # Install vertexai dependencies
    pip install google-cloud-aiplatform==1.62.0
    # Install langchain dependencies
    pip install langchain==0.2.14 langchain-google-vertexai==1.0.8
    # Install websocket
    pip install fastapi==0.112.1 uvicorn==0.30.6 websockets==13.0

    # Freeze the dependencies
    # pip freeze > requirements.txt
fi

# Deactivate the virtual environment
deactivate