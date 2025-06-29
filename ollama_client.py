"""Client for interacting with the Ollama API."""
from typing import Dict, List, Optional, Any
import httpx

from config import OLLAMA_HOST, REQUEST_TIMEOUT


class OllamaClient:
    """A client for interacting with the Ollama API."""
    
    def __init__(self, base_url: Optional[str] = None, timeout: Optional[int] = None) -> None:
        """Initialize the Ollama client.
        
        Parameters:
            base_url: Base URL for the Ollama server
            timeout: Request timeout in seconds
        """
        self.base_url = base_url or OLLAMA_HOST
        self.timeout = timeout or REQUEST_TIMEOUT
        self.client = httpx.Client(timeout=self.timeout)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
    
    def check_server(self) -> bool:
        """Check if the Ollama server is running and accessible.
        
        Returns:
            bool: True if server is accessible, False otherwise
        """
        try:
            response = self.client.get(f"{self.base_url}/api/version")
            return response.status_code == 200
        except Exception:
            return False
    
    def list_models(self) -> List[Dict[str, Any]]:
        """List all available Ollama models.
        
        Returns:
            List of model information dictionaries
        """
        try:
            response = self.client.get(f"{self.base_url}/api/tags")
            return (
                response.json().get('models', [])
                if response.status_code == 200
                else []
            )
        except Exception as e:
            print(f"Error listing models: {e}")
            return []
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        stream: bool = False,
        **options: Any
    ) -> Optional[Dict[str, Any]]:
        """Send chat messages to the Ollama API.
        
        Parameters:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use for the chat
            stream: Whether to stream the response
            **options: Additional options for the model
            
        Returns:
            Response from the Ollama API or None if there was an error
        """
        payload = {
            'model': model,
            'messages': messages,
            'stream': stream,
            'options': options
        }
        
        try:
            response = self.client.post(
                f"{self.base_url}/api/chat",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code != 200:
                print(f"Error from Ollama API: {response.status_code}")
                print(response.text)
                return None
                
            return response.json()
                
        except Exception as e:
            print(f"Error communicating with Ollama API: {e}")
            return None
