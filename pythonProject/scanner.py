import os
from dotenv import load_dotenv
import google.genai as genai


load_dotenv() # loads any secrets in the .env file
api_key = os.getenv("GOOGLE_API_KEY") # Retrieve your API Key from .env file
client = genai.Client(api_key=api_key) # Reads your API Key and sends it to Gemini

# Test with a simple prompt
try:
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite', contents='Why is the sky blue?'
    )
    print(response)
except Exception as e:
    print(f"❌ Connection failed: {e}")


