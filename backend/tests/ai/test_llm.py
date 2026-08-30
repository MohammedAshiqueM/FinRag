from backend.apps.ai.llm.factory import get_llm

def main():
    # Example prompt to test the LLM
    prompt = "Summarize the key risks Apple identified in its annual report."

    # Get LLM service based on settings.LLM_PROVIDER
    llm_service = get_llm()

    # Generate response
    try:
        response = llm_service.generate(prompt)

        print("=" * 80)
        print("PROMPT:")
        print(prompt)
        print("=" * 80)
        print("LLM RESPONSE:")
        print(response)
        print("=" * 80)

    except Exception as e:
        print("LLM generation failed:", str(e))


if __name__ == "__main__":
    main()
