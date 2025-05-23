import subprocess
import time
from langchain_ollama import ChatOllama

def start_ollama_serve():
    """
    Starts the "ollama serve" command as a subprocess.
    It will run in the background while the script continues.
    """
    try:
        # Start the "ollama serve" process.
        process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Optionally, wait a bit to give the server time to start up.
        time.sleep(2)
        print("Ollama server started successfully.")
        return process
    except Exception as e:
        print(f"Error starting ollama serve: {e}")
        return None

def get_nutrients(food_items):
    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0,
        num_predict=256,
    )

    messages = [
        (
            "human",
            (
                f"Sum up the approximate total nutrients of {food_items}. Avoid further questions. "
                "Make assumptions and use estimates. Return percentages of recommended daily intakes. "
                "Use this format 'Protein: ..g\nFat: ..g\nCarbohydrates: ..g'. Avoid details and sentences in your answer."
            )
        ),
    ]

    response = ""
    for chunk in llm.stream(messages):
        response += chunk.text()

    return response

def main():
    # Start the ollama server
    ollama_process = start_ollama_serve()

    # Get user input and process nutrients.
    food_items = input("Enter your meal: ")
    nutrients = get_nutrients(food_items)
    print(nutrients)

    # Optionally, terminate the ollama server after processing.
    if ollama_process:
        ollama_process.terminate()
        print("Ollama server terminated.")

if __name__ == "__main__":
    main()
