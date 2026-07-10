import os
import sys
import google.genai as genai
from dotenv import load_dotenv

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

# File path from command line: python scanner.py <file_path>
if len(sys.argv) < 2: # sys.argv to capture the filename you type after python3 scanner.py command.
    print("Usage: python scanner.py <file_path>")
    sys.exit(1)

code_path = sys.argv[1] # grabs the filename you have typed
with open(code_path, "r") as f: # open file for reading purpose
    code = f.read()  # reads all the code from that file into a variable called "code".

prompt = security_prompt.format(code=code)

try:
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite', contents=prompt
    )
    print(response.text)
    # initially it was print(response)- it was to give us response which has metadata
    # changed to print(response.text)- gives a much cleaner readable output
except Exception as e:
    print(f"❌ Connection failed: {e}")


