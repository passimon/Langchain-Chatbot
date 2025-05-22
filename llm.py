from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3.2:1b",
    temperature = 0,
    num_predict = 256,
    # other params ...
)

messages = [
    ("human", "Return the words Hello World!"),
]
for chunk in llm.stream(messages):
    print(chunk.text(), end="")