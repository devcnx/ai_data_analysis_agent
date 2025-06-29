"""Utility functions for the Ollama client application."""
from typing import Dict, Any, List


def format_model_info(models: List[Dict[str, Any]]) -> str:
    """Format model information for display.
    
    Args:
        models: List of model information dictionaries
        
    Returns:
        Formatted string with model information
    """
    if not models:
        return "No models found."
    
    result = ["\n📋 Available models:"]
    for model in models:
        name = model.get('name', 'unnamed')
        size = model.get('size', 0)
        size_gb = size / (1024 ** 3)  # Convert bytes to GB
        details = model.get('details', {})
        param_size = details.get('parameter_size', 'unknown')
        result.append(f"- {name} ({size_gb:.1f}GB, {param_size})")
    
    return "\n".join(result)


def format_chat_message(role: str, content: str) -> Dict[str, str]:
    """Create a properly formatted chat message.
    
    Args:
        role: Role of the message sender ('user', 'assistant', 'system')
        content: Content of the message
        
    Returns:
        Formatted message dictionary
    """
    return {
        'role': role,
        'content': content
    }
