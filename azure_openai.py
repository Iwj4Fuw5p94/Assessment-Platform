# azure_openai.py
from azure.ai.openai import ChatGPTClient
from azure.core.credentials import AzureKeyCredential
 
# Set up Azure OpenAI credentials (replace with your own keys)
endpoint = "https://YOUR_RESOURCE_NAME.openai.azure.com/"
api_key = "YOUR_API_KEY"
 
# Initialize the client
client = ChatGPTClient(endpoint, AzureKeyCredential(api_key))
 
# Function to generate a response using Azure OpenAI
def generate_response(prompt: str):
    response = client.completions.create(
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.result['choices'][0]['text']
 
# Test the AI model with a simple prompt
if __name__ == "__main__":
    prompt = "What is the capital of France?"
    answer = generate_response(prompt)
    print(f"AI Response: {answer}")

    
# CLI Output:
# AI Response: The capital of France is Paris.
