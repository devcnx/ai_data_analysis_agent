# AI Data Analysis Agent - Local Ollama Chat Client

This is a simple Python application designed to interact with the Ollama API for language generation. This application originally used OpenAI ChatGPT and OpenAI API keys, but has been updated to work with Ollama running locally.

## Features

- Connect to a local or remote Ollama server
- List available models
- Send chat messages to any available model
- Configurable model parameters (temperature, context length, etc.)
- Clean, modular codebase with type hints

## Prerequisites

- Python 3.8+
- Ollama server running locally or accessible via network

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd ollama-chat-client
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   uv venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   uv pip install --upgrade pip
   ```

3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

## Usage

1. Start the Ollama server if it's not already running:

   ```bash
   ollama serve
   ```

2. Run the chat client:
   ```bash
   python ai_data_analyst_ollama.py
   ```

### Environment Variables

- `OLLAMA_HOST`: The base URL of the Ollama server (default: `http://localhost:11434`)

## Project Structure

- `README.md`: Project description and usage instructions
- `requirements.txt`: Project dependencies
- `config.py`: Configuration settings and environment variable handling
- `utils.py`: Utility functions and helpers
- `ollama_client.py`: Client for interacting with the Ollama API
- `ai_data_analyst_ollama.py`: Main entry point for the chat client

## Example

```python
from ollama_client import OllamaClient

with OllamaClient() as client:
    if client.check_server():
        response = client.chat(
            messages=[{"role": "user", "content": "Why is the sky blue?"}],
            model="llama3:latest",
            temperature=0.7
        )
        print(response['message']['content'] if response else "No response")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
