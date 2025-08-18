"""Module for debugging Azure Speech Service Key Retrieval Issues."""

# Import Libraries
import os
from pathlib import Path
from dotenv import load_dotenv

# point to the .env file (make sure the name matches your file!)
dotenv_path = Path(__file__).parent / "speech.env"

# check if the .env (env variables file) exists
if not dotenv_path.exists():
    raise FileNotFoundError(
        f"Could not find the .env file at {dotenv_path}"
    )

# Load the .env file
load_dotenv(dotenv_path)

# Verify presence of environment variables
AZURE_KEY = os.getenv("AZURE_SPEECH_KEY")
REGION = os.getenv("AZURE_SPEECH_REGION")

if not AZURE_KEY or not REGION:
    raise EnvironmentError(
        "Azure credentials missing. Make sure AZURE_SPEECH_KEY and AZURE_SPEECH_REGION "
        "are set in your .env file."
    )

print(f"Loaded Azure credentials: REGION={REGION}, KEY starts with {AZURE_KEY[:5]}...")