from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """
    Abstract Base Class that defines the interface for all llm providers.
    
    Any concrete llm service (like ollamaLLM or OpenAILLM)
    must implement the `generate()` method as defined here.
    """
    @abstractmethod
    def generate(self, prompt:str) -> str:
        """
        Generate a response from the LLM based on the given prompt.
        
        Args:
            prompt: Input prompt string for the LLM
            
        Returns:
            Generated text response from the LLM
        """
        pass