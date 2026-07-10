import os
from dotenv import load_dotenv
import google.genai as genai


load_dotenv() # loads any secrets in the .env file
api_key = os.getenv("GOOGLE_API_KEY") # Retrieve your API Key from .env file
client = genai.Client(api_key=api_key)# Reads your API Key and sends it to Gemini


security_prompt = """
You are a security expert. Analyze this code for vulnerabilities.

For each issue, provide:
1. Vulnerability type
2. Why it is vulnerable (1 sentence)
3. Impact (1 sentence)
4. Secure code fix

Be concise.

Code:
{code}
"""

# Test with a simple prompt
try:
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite', contents= security_prompt
    )
    print(response)
except Exception as e:
    print(f"❌ Connection failed: {e}")


