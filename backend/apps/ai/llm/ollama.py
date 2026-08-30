from backend.apps.ai.llm.base import BaseLLM
import ollama


class OllamaLLM(BaseLLM):
    """
    Concrete implementation of BaseLLM using ollama llm.
    
    This class is responsible for loading the model and generating prompt result
    using the ollama models.
    """
    def __init__(self, model_name: str = 'phi3:mini'):
        self.model = model_name
        
    def generate(self, prompt):
        response = ollama.generate(
            model=self.model,
            prompt=prompt,
            options={
                'temperature': 0.3,  # Lower temperature for more focused summaries
                'num_predict': 200,  # Limit response length
            }
        )
        return response['response']
