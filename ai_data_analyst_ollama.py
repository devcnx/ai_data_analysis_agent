#!/usr/bin/env python3
"""Main entry point for the Ollama Chat Client."""
import sys
import time
import json
from typing import List, Dict, Any, Optional

from config import OLLAMA_HOST, DEFAULT_MODEL
from ollama_client import OllamaClient
from utils import format_model_info, format_chat_message


def check_ollama_server(client: OllamaClient) -> bool:
    """Check if Ollama server is running and accessible.
    
    Parameters:
        client: Initialized OllamaClient instance
        :type client: OllamaClient
        
    Returns:
        - True if server is accessible, False otherwise
        :rtype: bool
    """
    if client.check_server():
        print("✅ Connected to Ollama server")
        return True
    else:
        print("❌ Could not connect to Ollama server")
        print("Please make sure Ollama is running. You can start it with: ollama serve")
        return False


def list_available_models(client: OllamaClient) -> bool:
    """List all available Ollama models.
    
    Parameters:
        client: Initialized OllamaClient instance.
        :type client: OllamaClient
        
    Returns:
        - True if models are available, False otherwise
        :rtype: bool
    """
    models = client.list_models()
    if models:
        print(format_model_info(models))
        return True
    else:
        print("\nℹ️  No models found. Try pulling a model first with: ollama pull llama4:latest")
        return False


def chat_with_model(
    client: OllamaClient,
    prompt: str,
    model: str = None,
    **options
) -> Optional[Dict[str, Any]]:
    """Send a chat message to the specified model.
    
    Parameters:
        client: Initialized OllamaClient instance
        :type client: OllamaClient instance
        
        prompt: The user's message
        :type prompt: str
        
        model: Model to use (defaults to DEFAULT_MODEL)
        :type model: str
        
        **options: Additional options for the model
        :type options: Any
        
    Returns:
        - The model's response or None if there was an error
        :rtype: Optional[Dict[str, Any]]
    """
    messages = [format_chat_message('user', prompt)]
    
    print("\n🚀 Sending request to Ollama (this may take a moment)...")
    start_time = time.time()
    
    response = client.chat(
        messages=messages,
        model=model or DEFAULT_MODEL,
        **options
    )
    
    if response is None:
        print("\n❌ Failed to get a response from the model.")
        return None
    
    elapsed = time.time() - start_time
    print(f"\n✅ Response received in {elapsed:.2f} seconds")
    print("-" * 50)
    
    return response


def main():
    """Main function to run the Ollama chat client."""
    print(f"Using Ollama server at: {OLLAMA_HOST}")
    
    with OllamaClient() as client:
        print("🔍 Checking Ollama server...")
        if not check_ollama_server(client):
            sys.exit(1)
        
        print("\n📡 Fetching available models...")
        if not list_available_models(client):
            print("No models available. Please pull a model first with: ollama pull llama4:latest")
            sys.exit(1)
        
        try:
            # Example chat interaction
            prompt = "Why is the sky blue? Keep the answer brief."
            response = chat_with_model(
                client=client,
                prompt=prompt,
                temperature=0.7,
                num_ctx=2048
            )
            
            if response and 'message' in response and 'content' in response['message']:
                print(response['message']['content'])
            print(json.dumps(response, indent=4))
            
        except KeyboardInterrupt:
            print("\n🛑 Operation cancelled by user.")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {str(e)}")
            sys.exit(1)


if __name__ == "__main__":
    main()