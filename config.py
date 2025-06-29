"""Configuration settings for the Ollama Client."""
import os


def get_ollama_host() -> str:
    """Get the Ollama host URL with proper formatting.
    
    Returns:
        str: Formatted URL for the Ollama server
    """
    host = os.environ.get('OLLAMA_HOST', 'localhost')
    
    # Ensure the URL has a scheme (http:// or https://)
    if not host.startswith(('http://', 'https://')):
        host = f'http://{host}'
    
    # Ensure the URL has a port if not specified
    if ':' not in host.split('//')[-1]:
        host = f'{host}:11434'
    
    return host


# Global configuration
OLLAMA_HOST = get_ollama_host()
DEFAULT_MODEL = 'llama3:latest'  # Default model to use
REQUEST_TIMEOUT = 300  # 5 minutes in seconds
