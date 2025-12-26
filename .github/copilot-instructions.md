# Copilot Instructions for AccessLLM Project

## Project Overview
This is a multi-LLM learning and experimentation project containing Python scripts that demonstrate different approaches to accessing various Large Language Model (LLM) providers. Each file represents a standalone example for a specific provider.

## Architecture & File Organization
- **AccessLLM/**: Core directory containing provider-specific LLM interaction scripts
  - `OpenAILLM.py`: OpenAI GPT models via official OpenAI client
  - `GroqLLM.py`: Groq's fast inference API using Groq client  
  - `GeminiLLM.py`: Google's Gemini models via Google genai client
  - `OllamaLLM.py`: Local Ollama models for offline inference
- **Dependency Management**: Each script has its own virtual environment (`.venv/`)

## Key Patterns & Conventions

### API Key Management
API keys are now stored securely in environment variables using `.env` file:
```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API keys are automatically loaded from environment
# OPENAI_API_KEY, GOOGLE_API_KEY, GROQ_API_KEY
```

**Security Setup:**
- Copy `.env.example` to `.env` and add your actual API keys
- `.env` is in `.gitignore` to prevent accidental commits
- Use `.env.example` as a template for required environment variables

### Chat History Pattern
Scripts demonstrate different approaches to conversation continuity:
- **OpenAI/Groq**: Uses `messages` list with role-based chat history
- **Gemini**: Uses `chat.create()` and `send_message()` for persistent sessions
- **Ollama**: Direct message array approach

### Model Selection Examples
- OpenAI: `"gpt-3.5-turbo"`, `"gpt-4"`
- Groq: `"llama-3.3-70b-versatile"`  
- Gemini: `"gemini-2.5-flash"`, `"gemini-1.5-pro"`
- Ollama: `"gpt-oss:20b"` (local models)

## Development Workflow

### Environment Setup
```bash
cd AccessLLM
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your actual API keys
```

### Running Scripts
Each script is executable independently:
```bash
cd AccessLLM
python OpenAILLM.py
python GroqLLM.py  
python GeminiLLM.py
python OllamaLLM.py  # Requires Ollama running locally
```

## Provider-Specific Patterns

### OpenAI Integration
- Uses `client.chat.completions.create()` for chat completions
- Demonstrates multi-turn conversations by appending to `chat_history` list
- Shows both single and follow-up query patterns

### Groq Integration  
- Similar to OpenAI API structure but with Groq models
- Uses `client.chat.completions.create()` method
- Shows conversation continuation in a single request

### Gemini Integration
- Uses Google's genai client with different API structure
- `client.chats.create()` for persistent chat sessions
- `chat.send_message()` for continuing conversations
- Includes both direct generation and chat session patterns

### Ollama Integration
- Simplest pattern using `ollama.chat()` directly
- Requires local Ollama installation and model download
- Uses standard messages array format

## Key Considerations When Extending

1. **API Key Security**: API keys are stored in `.env` file and loaded via python-dotenv
2. **Error Handling**: Add try/catch blocks for API failures and rate limiting
3. **Model Variations**: Each provider has different model naming conventions
4. **Response Formats**: Response structures vary between providers
5. **Local vs. Remote**: Ollama requires local setup while others are cloud-based
6. **Environment Variables**: All scripts use `load_dotenv()` to load API keys from `.env`

## Testing Approach
- Each script contains hardcoded example prompts for immediate testing
- Run individual scripts to verify provider connectivity
- Check console output for successful API responses