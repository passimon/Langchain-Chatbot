from langchain_ollama import ChatOllama

class ChatBot:
    def __init__(self):
        self.llm = ChatOllama(
            model="llama3.2:1b",
            temperature=0,
            num_predict=256,
            # other params ...
        )

    def get_response(self, message):
        messages = [
            ("human", message),
        ]
        response = ""
        for chunk in self.llm.stream(messages):
            response += chunk.text()
        return response

    def start_chat(self):
        print("Welcome to the chatbot! Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break
            response = self.get_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.start_chat()
