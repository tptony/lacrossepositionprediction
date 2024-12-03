#setup virtual environment
#!/bin/bash

# Check if the LaxPred virtual environment exists
if [ ! -d "LaxPred" ]; then
    # Create the virtual environment
    python3 -m venv LaxPred
fi

# Activate the virtual environment
source LaxPred/bin/activate

# Install the requirements
# may need to add additional command depending on your OS
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
