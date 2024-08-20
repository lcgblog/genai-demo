#!/bin/bash
# Check if venv directory exists and delete it if it does
if [ -d "venv" ]; then
    rm -rf venv
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Check if requirements.txt is not empty and install the specified dependencies
if [ -s "requirements.txt" ]; then
    pip install -r requirements.txt
else
    # Install dependencies
    pip install google-cloud-aiplatform==0.3.0

    # Freeze the dependencies
    # pip freeze > requirements.txt
fi

# Deactivate the virtual environment
deactivate