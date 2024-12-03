#setup virtual environment
#!/bin/bash

# Check if the laxlens virtual environment exists
if [ ! -d "laxlens" ]; then
    # Create the virtual environment
    python3 -m venv laxlens
fi

# Activate the virtual environment
source laxlens/bin/activate

# Install the requirements
# may need to add additional command depending on your OS
pip install --upgrade pip
pip install -r requirements.txt
