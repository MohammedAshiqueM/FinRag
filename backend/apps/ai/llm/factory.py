from backend.apps.ai.llm.ollama import OllamaLLM
from backend.finrag import settings


def get_llm():
    """
    Factory function that returns the appropriate llm model 
    based on the LLM_PROVIDER configuration.
    
    This allows us to easily switch between different llm models
    without changing the business logic.
    """
    provider = settings.LLM_PROVIDER
    
    if provider == 'ollama':
        return OllamaLLM()
    
    raise ValueError(f"unknown provider {provider}")
